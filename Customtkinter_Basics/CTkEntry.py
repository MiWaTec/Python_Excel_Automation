import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Entry')

def enable_entry():
    entry4.configure(state='normal')

# CTkEntry
entry = ctk.CTkEntry(window,
                     fg_color='orange',
                     text_color='blue',
                     width=300,
                     height=50)
entry.grid(row=0, column=0, padx=125, pady=20)

entry2 = ctk.CTkEntry(window,
                      corner_radius=20,
                      placeholder_text='Enter your name',
                      placeholder_text_color='yellow')
entry2.grid(row=1, column=0, padx=20, pady=20)

entry3 = ctk.CTkEntry(window,
                      border_width=4,
                      border_color='crimson')
entry3.grid(row=2, column=0, padx=20, pady=20)

entry4 = ctk.CTkEntry(window,
                      state='disabled')
entry4.grid(row=3, column=0, padx=20, pady=20)

button = ctk.CTkButton(window,
                       text='Enable',
                       command= enable_entry)
button.grid(row=4, column=0, padx=20, pady=20)

# Wait for interaction with the GUI
window.mainloop()

entry4 = ctk.CTkEntry(window)
entry4.grid(row=3, column=0, padx=20, pady=20)