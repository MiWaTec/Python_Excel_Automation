import customtkinter as ctk
from PIL import Image

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Label')

# Label
label = ctk.CTkLabel(window,
                     text = 'This is a label',
                     fg_color='orange',
                     text_color='blue',
                     width = 100,
                     height = 50)
label.grid(row=0, column=0, padx=235, pady=50)

label2 = ctk.CTkLabel(window,
                      fg_color='red',
		      corner_radius=20)
label2.grid(row=1, column=0, padx=235, pady=50)


# Label with icon
icon = Image.open('BTN_Icon.png')
label_image = ctk.CTkImage(icon)

label3 = ctk.CTkLabel(window,
                      text='Label with image',
                      fg_color='purple',
                      width=50,
                      height=30,
                      image = label_image,
                      padx=20,
                      pady=10,
                      compound='left')
label3.grid(row=2, column=0, padx=235, pady=50)

label3 = ctk.CTkLabel(window,
                      text='Label with image',
                      fg_color='purple',
                      width=50,
                      height=30,)
label3.grid(row=2, column=0, padx=235, pady=50)

# Wait for interaction with the GUI
window.mainloop()