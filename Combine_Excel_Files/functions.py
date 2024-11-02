import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image

def browse_folder(input_line):
    """This function will open a window from which the folder can be chosen.
    """
    folder_path = filedialog.askdirectory()
    input_line.delete(0, tk.END)
    input_line.insert(tk.END, folder_path)


def getExcelFiles(folder_path) -> list:
    """This function searches for all excel files that are located inside the
       given folder and their subfolders. The paths of all found excel files
       will be returned as a list.
    Args:
        folder_path (str): Path to the folder that contains the result data
                           as excel files.

    Returns:
        excel_list (list): List that contains the paths of all found excel
                           files as strings.
    """
    excel_list = []
    for folder, subfolder, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xlsx'):
                excel_list.append((os.path.join(folder, file), file))
    return excel_list


def displayExcelList(scrollable_frame, select_all, excel_list, switch_state):
    # Load label icon
    icon = Image.open('Images/Excel_Icon_2.png')
    label_icon = ctk.CTkImage(icon)
    # Clear scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    # Reset 'Select all' switch to 0
    reset_switch(select_all)
    # Check display mode
    if switch_state == 0:
        displayExcelFiles(scrollable_frame, select_all, excel_list, label_icon)
    elif switch_state == 1:
        displayExcelWorksheets(scrollable_frame, select_all, excel_list, label_icon)


def displayExcelWorksheets(scrollable_frame, select_all, excel_list, label_icon):
    row_counter = 0
    for item in excel_list:
        label = ctk.CTkLabel(scrollable_frame,
                             text=item[1],
                             image=label_icon,
                             compound='left',
                             padx=5)
        label.grid(row=row_counter, column=0, padx=5, sticky='w')
        row_counter += 1
        # Get all worksheets
        excel_file = pd.ExcelFile(item[0])
        sheet_names = excel_file.sheet_names
        # Display worksheets
        for worksheet in sheet_names:
            checkbox_ws = ctk.CTkCheckBox(scrollable_frame,
                                          checkbox_width=20,
                                          checkbox_height=20,
                                          fg_color='#21A366',
                                          hover_color='#66E383',
                                          text=worksheet,
                                          command= lambda: reset_switch(select_all))
            checkbox_ws.grid(row=row_counter, column=0, padx=35, pady=[0, 0], sticky='w')
            row_counter += 1


def displayExcelFiles(scrollable_frame, select_all, excel_list, label_icon):
    for index, item in enumerate(excel_list):
        checkbox = ctk.CTkCheckBox(scrollable_frame,
                                   checkbox_width=25,
                                   checkbox_height=25,
                                   fg_color='#21A366',
                                   hover_color='#66E383',
                                   text=item[1],
                                   command= lambda: reset_switch(select_all))
        checkbox.grid(row=index, column=0, padx=5, pady=5, sticky='w')


def reset_switch(switch_widget):
    if switch_widget.get() == 1:
        switch_widget.deselect()


def toggle_all_checkboxes(switch_state, widgets):
    for widget in widgets:
        if isinstance(widget, ctk.CTkCheckBox):
            if switch_state == 0:
                widget.deselect()
            elif switch_state == 1:
                widget.select()


def combineExcelWorksheets(switch_state, available_files, input_path, output_path, output_name):
    # Create excel dict with file names as key and paths as values
    excel_file_paths = getExcelFiles(input_path)
    excel_dict = {}
    for excel in excel_file_paths:
        excel_dict[excel[1]] = excel[0]
    # Save the paths of the selected excel files into a dict
    selected_excel_dict = {}
    current_excel_file = None
    for widget in available_files.winfo_children():
        if isinstance(widget, ctk.CTkLabel):
            if widget.cget('text') in excel_dict:
                current_excel_file = widget.cget('text')
                excel_file = pd.ExcelFile(excel_dict[widget.cget('text')])
                selected_excel_dict[excel_dict[current_excel_file]] = []
        if isinstance(widget, ctk.CTkCheckBox):
            if widget.get() == 1:
                selected_excel_dict[excel_dict[current_excel_file]].append(widget.cget('text'))
    print(selected_excel_dict)
    # Merge excel worksheets
    mergeExcelData(switch_state, selected_excel_dict, output_path, output_name)


def combineExcelFiles(switch_state, available_files, input_path, output_path, output_name):
    # Create excel dict with file names as key and paths as values
    excel_file_paths = getExcelFiles(input_path)
    excel_dict = {}
    for excel in excel_file_paths:
        excel_dict[excel[1]] = excel[0]
    # Save the paths of the selected excel files into a dict
    selected_excel_dict = {}
    for widget in available_files.winfo_children():
        if isinstance(widget, ctk.CTkCheckBox) and widget.get() == 1:
            selected_excel_dict[widget.cget('text')] = excel_dict[widget.cget('text')]
    # Merge excel files
    mergeExcelData(switch_state, selected_excel_dict, output_path, output_name)

    # df_merged = None
    # for item in selected_excel_dict:
    #     df = pd.read_excel(selected_excel_dict[item])
    #     df_merged = pd.concat([df_merged, df], ignore_index=True, sort=False)
    # # Write dataframe into a new excel file
    # merged_excel = os.path.join(output_path, output_name + '.xlsx')
    # df_merged.to_excel(merged_excel, index=False)


def mergeExcelData(switch_state, selected_excel_dict, output_path, output_name):
    # Merge all selected excel files to a single dataframe
    df_merged = None
    # Case: Merge excel files
    if switch_state == 0:
        for item in selected_excel_dict:
            df = pd.read_excel(selected_excel_dict[item])
            df_merged = pd.concat([df_merged, df], ignore_index=True, sort=False)
    # Case: Merge excel worksheets
    if switch_state == 1:
        for item in selected_excel_dict:
            excel_file = pd.ExcelFile(item)
            for ws in selected_excel_dict[item]:
                df = excel_file.parse(ws)
                df_merged = pd.concat([df_merged, df], ignore_index=True, sort=False)
    # Write dataframe into a new excel file
    merged_excel = os.path.join(output_path, output_name + '.xlsx')
    df_merged.to_excel(merged_excel)


def mergeSelectedExcelData(switch_state, available_files, input_path, output_path, output_name):
    if switch_state == 0:
        combineExcelFiles(switch_state, available_files, input_path, output_path, output_name)
    elif switch_state == 1:
        combineExcelWorksheets(switch_state, available_files, input_path, output_path, output_name)

