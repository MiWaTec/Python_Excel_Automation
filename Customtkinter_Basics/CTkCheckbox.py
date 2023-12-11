import customtkinter as ctk

# Main window
window = ctk.CTk(fg_color='gray')
window.geometry('550x200')
window.title('Example App Title')

def get_state():
    print(checkbox4.get())


# CTkCheckBox
checkbox = ctk.CTkCheckBox(window, text='Checkbox',
                           text_color='blue',
                           fg_color='orange',
                           hover_color='yellow')
checkbox.grid(row=0, column=0, padx=20, pady=20)

checkbox2 = ctk.CTkCheckBox(window, text='Checkbox',
                            corner_radius=20)
checkbox2.grid(row=0, column=1, padx=10, pady=20)

checkbox3 = ctk.CTkCheckBox(window, text='Checkbox',
                            border_width=5,
                            border_color='red')
checkbox3.grid(row=0, column=2, padx=10, pady=20)

checkbox4 = ctk.CTkCheckBox(window, text='Checkbox',
                            onvalue='Checked',
                            offvalue='Unchecked',
                            command=get_state)
checkbox4.grid(row=0, column=3, padx=10, pady=20)

# Wait for interaction with the GUI
window.mainloop()