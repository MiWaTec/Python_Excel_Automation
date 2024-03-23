import tkinter as tk
import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('500x550')
window.title('Radio Button')

def radiobutton_clicked():
    print(radio_var.get())
    

# CTkRadioButton
radio_var = tk.IntVar(value=0)

radiobutton = ctk.CTkRadioButton(window,
                                 text= 'Radiobutton 1',
                                 variable=radio_var,
                                 value=1,
                                 command=radiobutton_clicked,
                                 text_color='magenta',
                                 fg_color='red',
                                 border_color='yellow',
                                 hover_color='aquamarine',
                                 hover=False)
radiobutton.grid(row=0, column=0, padx=200, pady=40)

radiobutton2 = ctk.CTkRadioButton(window,
                                 text= 'Radiobutton 2',
                                 variable=radio_var,
                                 value=2,
                                 command=radiobutton_clicked,
                                 border_width_unchecked=8,
                                 border_width_checked=8)
radiobutton2.grid(row=1, column=0, padx=200, pady=40)

radiobutton3 = ctk.CTkRadioButton(window,
                                 text= 'Radiobutton 3',
                                 variable=radio_var,
                                 value=3,
                                 command=radiobutton_clicked,
                                 radiobutton_width=20,
                                 radiobutton_height=20,
                                 corner_radius=1)
radiobutton3.grid(row=2, column=0, padx=200, pady=40)

# Wait for interaction with the GUI
window.mainloop()