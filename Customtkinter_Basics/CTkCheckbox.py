import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Example App Title')

def get_state():
    print(checkbox4.get())


# CTkCheckBox
checkbox = ctk.CTkCheckBox(window, text='Checkbox 1',
                           text_color='yellow',
                           text_color_disabled='gray', 
                           fg_color='orange',
                           hover_color='aqua')
checkbox.grid(row=0, column=0, padx=220, pady=30)

checkbox2 = ctk.CTkCheckBox(window, text='Checkbox 2',
                            corner_radius=20)
checkbox2.grid(row=1, column=0, padx=10, pady=30)

checkbox3 = ctk.CTkCheckBox(window, text='Checkbox 3',
                            border_width=5,
                            border_color='red')
checkbox3.grid(row=2, column=0, padx=10, pady=30)

checkbox4 = ctk.CTkCheckBox(window, text='Checkbox 4',
                            onvalue='Checked',
                            offvalue='Unchecked',
                            command=get_state)
checkbox4.grid(row=3, column=0, padx=10, pady=30)

# Wait for interaction with the GUI
window.mainloop()