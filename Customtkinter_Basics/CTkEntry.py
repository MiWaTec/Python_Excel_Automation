import customtkinter as ctk


# Main window
window = ctk.CTk(fg_color='gray')
window.geometry('550x200')
window.title('Example App Title')

# CTkEntry
entry = ctk.CTkEntry(window,
                     fg_color='orange',
                     text_color='black')
entry.grid(row=0, column=0, padx=20, pady=20)

entry2 = ctk.CTkEntry(window,
                      corner_radius=20,
                      placeholder_text='Entry your name',
                      placeholder_text_color='yellow')
entry2.grid(row=0, column=1, padx=20, pady=20)

entry3 = ctk.CTkEntry(window,
                      border_width=5,
                      border_color='red')
entry3.grid(row=0, column=2, padx=20, pady=20)

# Wait for interaction with the GUI
window.mainloop()