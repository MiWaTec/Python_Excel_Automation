import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('550x550')
window.title('Example App Title')

def seg_button_clicked(segment):
    print(segment)
    # seg_button.insert(2, 'New segment')
    # seg_button.delete(segment)
    # seg_button.move(0, segment)

# CTkSegmentedButton
segments = ['First', 'Second', 'Third']
segments2 = ['First', 'Second', 'Third', 'Forth', 'Fifth', 'Sixth']

seg_button = ctk.CTkSegmentedButton(window,
                                    values=segments,
                                    height=50,
                                    fg_color='darkred',
                                    unselected_color= 'purple',
                                    selected_color='magenta',
                                    selected_hover_color='red',
                                    text_color='yellow',
                                    border_width=10,
                                    command=seg_button_clicked)
seg_button.grid(row=0, column=0, padx=200, pady=50)

seg_button2 = ctk.CTkSegmentedButton(window,
                                     values=segments2,
                                     corner_radius=20,
                                     state='disabled')
seg_button2.grid(row=1, column=0, padx=100, pady=50)

# Wait for interaction with the GUI
window.mainloop()
