import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk

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


def displayExcelFiles(scrollable_frame, excel_list):
    for index, item in enumerate(excel_list):
        checkbox = ctk.CTkCheckBox(scrollable_frame, text=item[1])
        checkbox.grid(row=index, column=0, padx=5, pady=[5, 0], sticky='w')


def combine_excel_files(available_files, input_path, output_path, output_name):
    # Create excel dict with file names as key and paths as values
    excel_file_paths = getExcelFiles(input_path)
    excel_dict = {}
    for excel in excel_file_paths:
        excel_dict[excel[1]] = excel[0]
    # Save the paths of the selected excel files into a list
    selected_excel_list = []
    for checkbox in available_files.winfo_children():
        if checkbox.get() == 1:
            path = excel_dict[checkbox.cget('text')]
            selected_excel_list.append(path)
    # Merge all selected excel files to a single dataframe
    df_merged = None
    for excel_file in selected_excel_list:
        df = pd.read_excel(excel_file)
        df_merged = pd.concat([df_merged, df], ignore_index=True, sort=False)
    # Write dataframe into a new excel file
    merged_excel = os.path.join(output_path, output_name + '.xlsx')
    print(merged_excel)
    df_merged.to_excel(merged_excel)
    return df_merged