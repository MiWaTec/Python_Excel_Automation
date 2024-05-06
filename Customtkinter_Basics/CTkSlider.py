import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Example App Title')

def slider_event(value):
    print(value)

# CTkSlider
slider = ctk.CTkSlider(window,
                       command=slider_event,
                       number_of_steps=100,
                       from_=0,
                       to=100)
slider.grid(row=0, column=0, padx=180, pady=50)

slider2 = ctk.CTkSlider(window,
                        width=150,
                        height=50)
slider2.grid(row=1, column=0, padx=180, pady=50)

slider3 = ctk.CTkSlider(window,
                        border_color='yellow',
                        border_width=2,
                        fg_color='aquamarine',
                        progress_color='blue',
                        button_color='orange',
                        button_hover_color='red',
                        hover=False,
                        orientation='vertical',
                        state='disable')
slider3.grid(row=2, column=0, padx=180, pady=50)

# Wait for interaction with the GUI
window.mainloop()