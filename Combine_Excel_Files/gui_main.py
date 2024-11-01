import customtkinter as ctk
from PIL import Image, ImageTk
import functions as func
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Create window
window = ctk.CTk()
window.geometry('750x605')
window.resizable(False, False)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=2)
window.title('Excel File Merger')

# Add image
src_img = Image.open('Images/Excel_Design_2.jpg')
src_img = src_img.resize((200, 740))
image = ImageTk.PhotoImage(src_img)

img_frame = ctk.CTkFrame(window)
img_frame.grid(row=0, column=0, rowspan=3, padx=(5, 2), pady=(5, 5))
img_frame.columnconfigure(1, weight=1)

img_label = ctk.CTkLabel(img_frame,
                         image=image)
img_label.grid(row=0, column=0)

# Set color
frame_color = '#1F9B69'

# Select folder and search for files
frame_select_folder = ctk.CTkFrame(window, fg_color=frame_color)
frame_select_folder.grid(row=0, column=1, padx=5, pady=5, sticky='we')
frame_select_folder.columnconfigure(1, weight=1)

title_label = ctk.CTkLabel(frame_select_folder, text='Select folder:',
                           font=ctk.CTkFont(size=12, weight='bold'))
title_label.grid(row=0, column=1, padx=[20, 0], sticky='ws')

input_folder = ctk.CTkEntry(frame_select_folder)
input_folder.grid(row=1, column=1, padx=[20, 0], pady=[0, 15], sticky='we')

btn_browse = ctk.CTkButton(frame_select_folder, text='Browse',
                           width=75,
                           fg_color='#06361B',
                           hover_color='#66E383',
                           command=lambda: [func.browse_folder(input_folder),
                                            func.displayExcelList(
                                                scrollable_frame,
                                                select_all,
                                                func.getExcelFiles(input_folder.get()),
                                                display_mode.get())])
btn_browse.grid(row=1, column=2, padx=[0, 20], pady=[0, 15])

# Select excel files
frame_select_files = ctk.CTkFrame(window,
                                  fg_color=frame_color)
frame_select_files.grid(row=1, column=1, padx=5, pady=5, sticky='we')
frame_select_files.columnconfigure(1, weight=1)

select_files_label = ctk.CTkLabel(frame_select_files,
                                  text='Select Excel files:',
                                  font=ctk.CTkFont(size=12, weight='bold'))
select_files_label.grid(row=0, column=0, padx=[20, 0], pady=[0, 0], sticky='w')

scrollable_frame = ctk.CTkScrollableFrame(frame_select_files,
                                          scrollbar_button_hover_color='#66E383',
                                          height=295)
scrollable_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=[0, 15], sticky='we')

select_all = ctk.CTkSwitch(frame_select_files,
                           text='Select all',
                           font=ctk.CTkFont(size=12, weight='bold'),
                           button_color='#06361B',
                           progress_color='#66E383',
                           hover=False,
                           command=lambda: func.toggle_all_checkboxes(select_all.get(),
                                                                      scrollable_frame.winfo_children()))
select_all.grid(row=2, column=0, padx=20, pady=[0, 15], sticky='w')

display_mode = ctk.CTkSwitch(frame_select_files,
                           text='Display worksheets',
                           font=ctk.CTkFont(size=12, weight='bold'),
                           button_color='#06361B',
                           progress_color='#66E383',
                           hover=False,
                           command=lambda: func.displayExcelList(scrollable_frame,
                                                                 select_all,
                                                                 func.getExcelFiles(input_folder.get()),
                                                                 display_mode.get()))
display_mode.grid(row=2, column=1, padx=20, pady=[0, 15], sticky='w')

# Combine excel files
frame_combine_files = ctk.CTkFrame(window, fg_color=frame_color)
frame_combine_files.grid(row=2, column=1, padx=5, pady=5, sticky='we')
frame_combine_files.columnconfigure(1, weight=1)

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='Save merged Excel file in:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=0, column=1, padx=[20, 0], sticky='ws')

input_save_merged_excel = ctk.CTkEntry(frame_combine_files)
input_save_merged_excel.grid(row=1, column=1, padx=[20, 0], sticky='we')

btn_browse_save_folder = ctk.CTkButton(frame_combine_files, text='Browse',
                                       width=75,
                                       fg_color='#06361B',
                                       hover_color='#66E383',
                                       command=lambda:
                                       func.browse_folder(input_save_merged_excel))
btn_browse_save_folder.grid(row=1, column=2, padx=[0, 20], sticky='we')

save_in_folder_label = ctk.CTkLabel(frame_combine_files,
                                    text='File name:',
                                    font=ctk.CTkFont(size=12, weight='bold'))
save_in_folder_label.grid(row=2, column=1, padx=[20, 0], sticky='ws')

input_save_combined_excel = ctk.CTkEntry(frame_combine_files)
input_save_combined_excel.grid(row=3, column=1, padx=[20, 0], pady=[0, 15],
                               sticky='we')

btn_search_files = ctk.CTkButton(frame_combine_files,
                                 width=75, text='Merge',
                                 fg_color='#06361B',
                                 hover_color='#66E383',
                                 command=lambda: func.combineExcelFiles(scrollable_frame,
                                                                        input_folder.get(),
                                                                        input_save_merged_excel.get(),
                                                                        input_save_combined_excel.get()))
btn_search_files.grid(row=3, column=2, padx=[0, 20], pady=[0, 15])

# Wait for interaction with the GUI
window.mainloop()
