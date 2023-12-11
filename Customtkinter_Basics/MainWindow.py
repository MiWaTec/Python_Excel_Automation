import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Example App Title')
# window.columnconfigure(0, weight=1)

# Appearance modes
# ctk.set_appearance_mode("light")
ctk.set_appearance_mode("system")
# ctk.set_appearance_mode("dark")

# Wait for interaction with the GUI
window.mainloop()
