import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Scrollable Frame')

# CTkScrollableFrame
scrollable_frame = ctk.CTkScrollableFrame(window,
                                          width=300,
                                          height=300,
                                          corner_radius=30,
                                          border_width=5,
                                          border_color='orange',
                                          fg_color='tomato',
                                          scrollbar_fg_color='green2',
                                          scrollbar_button_color='red',
                                          scrollbar_button_hover_color='magenta',
                                          label_text='Example label text',
                                          label_font=('Impact', 20),
                                          label_text_color='aquamarine',
                                          label_fg_color='blue4',
                                          label_anchor='center',
                                          orientation="horizontal"
                                          )
scrollable_frame.grid(row=0, column=0, padx=90, pady=50)

button = ctk.CTkButton(scrollable_frame,
                       text='Button')
button.grid(row=0, column=0, padx=80, pady=40)

slider = ctk.CTkSlider(scrollable_frame)
slider.grid(row=1, column=0, padx=50, pady=40)

switch = ctk.CTkSwitch(scrollable_frame)
switch.grid(row=2, column=0, padx=80, pady=40)

# Wait for interaction with the GUI
window.mainloop()