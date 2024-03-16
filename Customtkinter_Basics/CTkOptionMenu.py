import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('500x650')
window.title('Option Menu')

def optionmenu_pressed(option):
    print(option)

# CTkOptionMenu
option_list = ['Option 1', 'Option 2', 'Option 3']

optionmenu = ctk.CTkOptionMenu(window,
                               values=option_list,
                               fg_color='purple',
                               text_color='yellow',
                               button_color='red',
                               button_hover_color='yellow',
                               hover=False,
                               command=optionmenu_pressed)
optionmenu.grid(row=0, column=0, padx=200, pady=25)

# optionmenu2 = ctk.CTkOptionMenu(window,
# 			                      values=option_list,
#                                 border_width=5,
#                                 border_color='orange')
# optionmenu2.grid(row=1, column=0, padx=20, pady=50)

optionmenu3 = ctk.CTkOptionMenu(window,
                                values=option_list,
                                corner_radius=20,
                                dropdown_fg_color='greenyellow',
			                    dropdown_text_color='blue',
                                dropdown_hover_color='magenta')
optionmenu3.grid(row=2, column=0, padx=20, pady=50)

# Wait for interaction with the GUI
window.mainloop()