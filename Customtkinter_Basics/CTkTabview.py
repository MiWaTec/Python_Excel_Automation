import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Tabview')

def selected_tab():
    visible_tab = tabview.get()
    print(visible_tab)

# CTkSwitch
tabview = ctk.CTkTabview(window,
                         width=500,
                         height=500,
                         corner_radius=30,
                         border_width=5,
                         border_color='red',
                         fg_color='orange',
                         segmented_button_fg_color='magenta',
                         segmented_button_selected_color='indigo',
                         segmented_button_selected_hover_color='deeppink4',
                         segmented_button_unselected_color='green',
                         segmented_button_unselected_hover_color='darkturquoise',
                         text_color='yellow',
                         anchor='se',
                         command=selected_tab)
# tabview.grid(row=0, column=0, padx=125, pady=50)
tabview.grid(row=0, column=0, padx=25, pady=25)

tab_1 = tabview.add('Tab 1')
tab_2 = tabview.add('Tab 2')
tab_3 = tabview.add('Tab 3')

button = ctk.CTkButton(tab_1)
button.grid(row=0, column=0, padx=73, pady=75)

slider = ctk.CTkSlider(tab_2)
slider.grid(row=0, column=0, padx=43, pady=75)

switch = ctk.CTkSwitch(tab_3)
switch.grid(row=0, column=0, padx=90, pady=75)

# Wait for interaction with the GUI
window.mainloop()