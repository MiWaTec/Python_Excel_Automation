import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('500x650')
window.title('Example App Title')

# CTkFrame
frame_1 = ctk.CTkFrame(window,
                       fg_color='greenyellow', 
                       border_width=10,
                       border_color='blue')
frame_1.grid(row=0, column=0, padx=25, pady=25)

frame_2 = ctk.CTkFrame(window,
                       fg_color='greenyellow')
frame_2.grid(row=0, column=1, padx=25, pady=25)

frame_3 = ctk.CTkFrame(window,
                       fg_color='greenyellow',
                       width=450,
                       height=350)
frame_3.grid(row=1, column=0, columnspan=2, padx=25, pady=25)

button_1 = ctk.CTkButton(frame_1,
                         text='Button 1')
button_1.grid(row=0, column=0, padx=30, pady=20)

button_2 = ctk.CTkButton(frame_1,
                         text='Button 2')
button_2.grid(row=1, column=0, padx=30, pady=20)

button_3 = ctk.CTkButton(frame_1,
                         text='Button 3')
button_3.grid(row=2, column=0, padx=30, pady=20)

# Wait for interaction with the GUI
window.mainloop()