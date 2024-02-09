import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Combobox')

def combobox_pressed(option):
    print(option)

# CTkComboBox
option_list = ['Option 1', 'Option 2', 'Option 3']

combobox = ctk.CTkComboBox(window,
                           values=option_list,
                           fg_color='purple',
                           text_color='yellow',
                           button_color='red',
                           button_hover_color='yellow',
                           hover=False,
                           command=combobox_pressed)
combobox.grid(row=0, column=0, padx=200, pady=50)

combobox2 = ctk.CTkComboBox(window,
			                values=option_list,
                            border_width=5,
                            border_color='orange')
combobox2.grid(row=1, column=0, padx=20, pady=50)

combobox3 = ctk.CTkComboBox(window,
                            values=option_list,
                            corner_radius=20,
                            dropdown_fg_color='greenyellow',
			    dropdown_text_color='blue',
                            dropdown_hover_color='magenta')
combobox3.grid(row=2, column=0, padx=20, pady=50)

# Wait for interaction with the GUI
window.mainloop()