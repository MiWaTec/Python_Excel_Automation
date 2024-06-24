import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Textbox')

# CTkTextbox
textbox = ctk.CTkTextbox(window,
                         width=450,
                         height=150,
                         border_width=5,
                         border_color='blue',
                         border_spacing=30,
                         corner_radius=50,
                         fg_color='black',
                         text_color='gold',
                         font=('Arial', 30),
                         scrollbar_button_color='red',
                         scrollbar_button_hover_color='yellow',
                         activate_scrollbars=False,
		                 wrap='char',
                         state='disabled')
textbox.grid(row=0, column=0, padx=50, pady=50)

# Wait for interaction with the GUI
window.mainloop()