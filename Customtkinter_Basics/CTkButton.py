import customtkinter as ctk
import random
from PIL import Image

def button1_pressed():
    color_list = ['red', 'blue', 'green', 'yellow']
    random_color = random.choice(color_list)
    button1.configure(hover_color=random_color)
    

# Main window
window = ctk.CTk()
window.geometry('550x700')
window.title('Example App Title')

# Template
button7 = ctk.CTkButton(window, text='Right',
                        image=btn_image
                        )
button7.grid(row=6, column=0, padx=205, pady=20)

# CTkButton
button1 = ctk.CTkButton(window,
                        text='Button 1',
                        command=button1_pressed)
button1.grid(row=0, column=0, padx=205, pady=20)

button2 = ctk.CTkButton(window,
                        text='Button 2',
                        width=75,
                        height=75)
button2.grid(row=1, column=0, padx=205, pady=20)

button3 = ctk.CTkButton(window, text='Button 3',
                       text_color='#ffb005',
                       fg_color='#672c8a',
                       hover_color='#cf4ea8'
                       )
button3.grid(row=2, column=0, padx=205, pady=20)

button4 = ctk.CTkButton(window, text='Button 4',
                        border_width=3,
                        border_color='#05fa7f'
                        )
button4.grid(row=3, column=0, padx=205, pady=20)

button5 = ctk.CTkButton(window, text='Button 5',
                        corner_radius=20
                        )
button5.grid(row=4, column=0, padx=205, pady=20)

#CTkButton with icon
btn_image = ctk.CTkImage(Image.open('BTN_Icon.png'))

button6 = ctk.CTkButton(window, text='Left (default)',
                        image=btn_image,
                        compound='left'
                        )
button6.grid(row=5, column=0, padx=205, pady=20)

button7 = ctk.CTkButton(window, text='Right',
                        image=btn_image,
                        compound='right'
                        )
button7.grid(row=6, column=0, padx=205, pady=20)

button8 = ctk.CTkButton(window, text='Top',
                        image=btn_image,
                        compound='top'
                        )
button8.grid(row=7, column=0, padx=205, pady=20)

button9 = ctk.CTkButton(window, text='Bottom',
                        image=btn_image,
                        compound='bottom'
                        )
button9.grid(row=8, column=0, padx=205, pady=20)

# Wait for interaction with the GUI
window.mainloop()