import customtkinter as ctk

# Main window
window = ctk.CTk(fg_color='gray')
window.geometry('550x200')
window.title('Example App Title')

# CTkComboBox
option_list = ['Option 1', 'Option 2', 'Option 3']

combobox = ctk.CTkComboBox(window, values=option_list,
                            fg_color='green',
                            button_color='red',
                            button_hover_color='yellow',
                            text_color='yellow'
                           )
combobox.grid(row=0, column=0, padx=20, pady=20)

combobox2 = ctk.CTkComboBox(window, values=option_list,
                            border_width=3,
                            border_color='orange'
                           )
combobox2.grid(row=0, column=1, padx=20, pady=20)

combobox3 = ctk.CTkComboBox(window, values=option_list,
                            corner_radius=20,
                            dropdown_fg_color='orange',
                            dropdown_hover_color='yellow',
                            dropdown_text_color='black'
                            )
combobox3.grid(row=0, column=2, padx=20, pady=20)

# Wait for interaction with the GUI
window.mainloop()