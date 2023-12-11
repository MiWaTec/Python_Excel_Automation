import customtkinter as ctk

# Create window
window = ctk.CTk()
window.geometry('500x480')
window.columnconfigure(0, weight=1)
window.title('Combine Excel Files')

# Set color
frame_color = '#300666'

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