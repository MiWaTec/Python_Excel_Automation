import customtkinter as ctk
import functions as func


# Create window
window = ctk.CTk()
window.geometry('500x480')
window.columnconfigure(0, weight=1)
window.title('Combine Excel Files')

frame_color = '#6910b3'

# Select folder and search for files
frame_select_folder = ctk.CTkFrame(window, fg_color=frame_color)
frame_select_folder.grid(row=0, column=0, padx=5, pady=5, sticky='we')
frame_select_folder.columnconfigure(0, weight=1)

title_label = ctk.CTkLabel(frame_select_folder, text='Select folder:',
                           font=ctk.CTkFont(size=12, weight='bold'))
title_label.grid(row=0, column=0, padx=[20, 0], sticky='ws')

input_folder = ctk.CTkEntry(frame_select_folder)
input_folder.grid(row=1, column=0, padx=[20, 0], pady=[0, 15], sticky='we')

btn_browse = ctk.CTkButton(frame_select_folder, text='Browse',
                           width=75,
                           command=lambda: [func.browse_folder(input_folder),
                                            func.displayExcelFiles(scrollable_frame, func.getExcelFiles(input_folder.get()))])
btn_browse.grid(row=1, column=1, padx=[0, 20], pady=[0, 15])

# Select excel files
frame_select_files = ctk.CTkFrame(window, fg_color=frame_color)
frame_select_files.grid(row=1, column=0, padx=5, pady=5, sticky='we')
frame_select_files.columnconfigure(0, weight=1)

select_files_label = ctk.CTkLabel(frame_select_files,
                                  text='Select Excel files:',
                                  font=ctk.CTkFont(size=12, weight='bold'))
select_files_label.grid(row=0, column=0, padx=[20, 0], pady=[0, 0], sticky='w')

scrollable_frame = ctk.CTkScrollableFrame(frame_select_files)
scrollable_frame.grid(row=1, column=0, padx=20, pady=[0, 15], sticky='we')

# Combine excel files
frame_combine_files = ctk.CTkFrame(window, fg_color=frame_color)
frame_combine_files.grid(row=2, column=0, padx=5, pady=5, sticky='we')
frame_combine_files.columnconfigure(0, weight=1)

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='Save merged Excel file in:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=0, column=0, padx=[20, 0], sticky='ws')

input_save_merged_excel = ctk.CTkEntry(frame_combine_files)
input_save_merged_excel.grid(row=1, column=0, padx=[20, 0], sticky='we')

btn_browse_save_folder = ctk.CTkButton(frame_combine_files, text='Browse',
                                       width=75,
                                       command=lambda:
                                       func.browse_folder(input_save_merged_excel))
btn_browse_save_folder.grid(row=1, column=1, padx=[0, 20], sticky='we')

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='File name:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=2, column=0, padx=[20, 0], sticky='ws')

input_save_combined_excel = ctk.CTkEntry(frame_combine_files)
input_save_combined_excel.grid(row=3, column=0, padx=[20, 0], pady=[0, 15],
                               sticky='we')

btn_search_files = ctk.CTkButton(frame_combine_files,
                                 width=75, text='Merge',
                                 command=lambda: func.combine_excel_files(scrollable_frame,
                                                                     input_folder.get(),
                                                                     input_save_merged_excel.get(),
                                                                     input_save_combined_excel.get()))
btn_search_files.grid(row=3, column=1, padx=[0, 20], pady=[0, 15])

# Wait for interaction with the GUI
window.mainloop()
