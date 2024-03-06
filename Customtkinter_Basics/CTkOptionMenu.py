import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('500x650')
window.title('Option Menu')

# CTkOptionMenu
option_list = ['Option 1', 'Option 2', 'Option 3']

optionmenu = ctk.CTkOptionMenu(window, values=option_list)
optionmenu.grid(row=0, column=0, padx=25, pady=25)

# Wait for interaction with the GUI
window.mainloop()