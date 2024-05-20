import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Switch')

def switch_on():
    state = switch.get()
    print(state)

# CTkSwitch
switch = ctk.CTkSwitch(window,
                       text='Example Switch',
                       command=switch_on,
                       onvalue='ON',
                       offvalue='OFF')
switch.grid(row=0, column=0, padx=230, pady=50)

switch2 = ctk.CTkSwitch(window,
                        switch_width=70,
                        switch_height=30,
                        corner_radius=5,
                        border_color='red',
                        border_width=8)
switch2.grid(row=1, column=0, padx=230, pady=50)

switch3 = ctk.CTkSwitch(window,
                        fg_color='green',
                        progress_color='yellow',
                        button_color='orange',
                        button_hover_color='magenta',
                        hover=False,
                        state='disabled')
switch3.grid(row=2, column=0, padx=230, pady=50)

# Wait for interaction with the GUI
window.mainloop()