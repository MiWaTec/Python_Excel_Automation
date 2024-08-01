import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Scrollbar')

# CTkScrollbar
textbox = ctk.CTkTextbox(window,
                         width=400,
                         height=200,
                         font=('Helvetica', 20),
			 activate_scrollbars=False,
			 wrap='none')
textbox.grid(row=0, column=0, padx=(60, 0), pady=(50, 0))

scrollbar = ctk.CTkScrollbar(window,
                             command=textbox.yview,
                             width=20,
                             height=100,
                             fg_color='SkyBlue2',
                             button_color='cyan4',
                             button_hover_color='aquamarine2',
                             hover=False,
			                 corner_radius=0,
			                 border_spacing=5,
                             minimum_pixel_length=50,
                             orientation='horizontal')
scrollbar.grid(row=0, column=1, padx=(0, 0), pady=(50, 0))

# Connect textbox scroll event to CTk scrollbar
textbox.configure(yscrollcommand=scrollbar.set)

# Wait for interaction with the GUI
window.mainloop()

# Hello world!

textbox = ctk.CTkTextbox(window,
                         width=400,
                         height=200,
                         font=('Helvetica', 30))
textbox.grid(row=0, column=0, padx=(60, 0), pady=(50, 0))