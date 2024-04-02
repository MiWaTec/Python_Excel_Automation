import customtkinter as ctk

# Main window
window = ctk.CTk()
window.geometry('500x550')
window.title('Progress Bar')

def stop_progressbar():
    progressbar.stop()

# CTkProgressBar
progressbar = ctk.CTkProgressBar(window,
                                 width=150,
                                 height=20,
                                 fg_color="yellow",
                                 progress_color="green",
                                 border_width=5,
                                 border_color="red",
                                 mode="determinate",
                                 determinate_speed=1)
progressbar.grid(row=0, column=0, padx=150, pady=100)

progressbar2 = ctk.CTkProgressBar(window,
                                  corner_radius=1,
                                  mode="indeterminate",
                                  indeterminate_speed=2)
progressbar2.grid(row=1, column=0, padx=150, pady=100)

# Wait for interaction with the GUI
progressbar.set(0)
progressbar.start()
progressbar.after(5000, progressbar.stop)
print(progressbar.get())

progressbar2.set(0)
progressbar2.start()
progressbar2.after(5000, progressbar2.stop)
print(progressbar.get())

window.mainloop()

