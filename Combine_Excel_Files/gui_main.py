import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import os
import pandas as pd


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
            if file.endswith('.xlsx') or file.endswith('.xls'):
                excel_list.append((os.path.join(folder, file), file))
    return excel_list


def displayExcelFiles(excel_list):
    for index, item in enumerate(excel_list):
        checkbox = ctk.CTkCheckBox(available_files, text=item[1],
                                   fg_color='#35A29F',
                                   hover_color='#97FEED')
        checkbox.grid(row=index, column=0, padx=5, pady=[5, 0], sticky='w')


def combine_excel_files(available_files, input_path, output_path, output_name):
    # Create excel dict with file names as key and paths as values
    excel_file_paths = getExcelFiles(input_path)
    excel_dict = {}
    for excel in excel_file_paths:
        print(excel[0])
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
    df_merged.to_excel(merged_excel)
    return df_merged


# Create window
window = ctk.CTk()
window.geometry('500x535')
window.columnconfigure(0, weight=1)
window.title('Combine Excel Files')
ctk.set_default_color_theme("green")

# Select folder and search for files
frame_select_folder = ctk.CTkFrame(window, fg_color=('#071952'))
frame_select_folder.grid(row=0, column=0, padx=5, pady=5, sticky='we')
frame_select_folder.columnconfigure(0, weight=1)

title_label = ctk.CTkLabel(frame_select_folder, text='Select folder:',
                           font=ctk.CTkFont(size=12, weight='bold'))
title_label.grid(row=0, column=0, padx=[20, 0], sticky='ws')

input_folder = ctk.CTkEntry(frame_select_folder)
input_folder.grid(row=1, column=0, padx=[20, 0], sticky='we')

btn_browse = ctk.CTkButton(frame_select_folder, text='Browse',
                           width=75, fg_color='#0B666A',
                           hover_color='#35A29F',
                           command=lambda: browse_folder(input_folder))
btn_browse.grid(row=1, column=1, padx=[0, 20])

btn_search_files = ctk.CTkButton(frame_select_folder, fg_color='#0B666A',
                                 text='Search Excel Files',
                                 hover_color='#35A29F',
                                 command=lambda:
                                 displayExcelFiles(getExcelFiles(input_folder.get())))
btn_search_files.grid(row=2, column=0, padx=[20, 0], pady=[15, 15],
                      sticky='w')

# Select excel files
frame_select_files = ctk.CTkFrame(window, fg_color=('#071952'))
frame_select_files.grid(row=1, column=0, padx=5, pady=5, sticky='we')
frame_select_files.columnconfigure(0, weight=1)

select_files_label = ctk.CTkLabel(frame_select_files,
                                  text='Select Excel files:',
                                  font=ctk.CTkFont(size=12, weight='bold'))
select_files_label.grid(row=0, column=0, padx=[20, 0], pady=[5, 0], sticky='w')

available_files = ctk.CTkScrollableFrame(frame_select_files,
                                         scrollbar_button_color='#0B666A',
                                         scrollbar_button_hover_color='#97FEED'
                                         )
available_files.grid(row=1, column=0, padx=20, pady=[5, 15], sticky='we')

# Combine excel files
frame_combine_files = ctk.CTkFrame(window, fg_color=('#071952'))
frame_combine_files.grid(row=2, column=0, padx=5, pady=5, sticky='we')
frame_combine_files.columnconfigure(0, weight=1)

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='Save merged Excel file in:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=0, column=0, padx=[20, 0], sticky='ws')

input_save_merged_excel = ctk.CTkEntry(frame_combine_files)
input_save_merged_excel.grid(row=1, column=0, padx=[20, 0], sticky='we')

btn_browse_save_folder = ctk.CTkButton(frame_combine_files, text='Browse',
                                       width=75, fg_color='#0B666A',
                                       hover_color='#35A29F',
                                       command=lambda:
                                       browse_folder(input_save_merged_excel))
btn_browse_save_folder.grid(row=1, column=1, padx=[0, 20], sticky='we')

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='File name:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=2, column=0, padx=[20, 0], sticky='ws')

input_save_combined_excel = ctk.CTkEntry(frame_combine_files)
input_save_combined_excel.grid(row=3, column=0, padx=[20, 0], pady=[0, 15],
                               sticky='we')

btn_search_files = ctk.CTkButton(frame_combine_files, fg_color='#0B666A',
                                 width=75, text='Merge', hover_color='#35A29F',
                                 command=lambda: combine_excel_files(available_files,
                                                                     input_folder.get(),
                                                                     input_save_merged_excel.get(),
                                                                     input_save_combined_excel.get()))
btn_search_files.grid(row=3, column=1, padx=[0, 20], pady=[0, 15])

# Wait for interaction with the GUI
window.mainloop()
