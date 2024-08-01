import tkinter
from tkinter import ttk
#import tkinterDnD

#customtkinter.set_ctk_parent_class(tkinterDnD.Tk)



app = tkinter.Tk()
app.geometry("400x780")
app.title("CustomTkinter simple_example.py")

#print(type(app), isinstance(app, tkinterDnD.Tk))

def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = tkinter.Frame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = ttk.Progressbar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = tkinter.Button(master=frame_1, command=button_callback, width=30, text="Button")
button_1.pack(pady=10, padx=10)

slider_1 = tkinter.Scale(master=frame_1, command=slider_callback, from_=0, to=1, orient="horizontal")
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = tkinter.Entry(master=frame_1, textvariable="Entry")
entry_1.pack(pady=10, padx=10)

value_inside = tkinter.StringVar(app)
value_inside.set("Select an Option")
optionmenu_1 = tkinter.OptionMenu(frame_1, value_inside, ["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
#optionmenu_1.set("CTkOptionMenu")

combobox_1 = ttk.Combobox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = tkinter.Checkbutton(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

radiobutton_1 = tkinter.Radiobutton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = tkinter.Radiobutton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

# switch_1 = tkinter.Switch(master=frame_1)
# switch_1.pack(pady=10, padx=10)

text_1 = tkinter.Text(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

# segmented_button_1 = tkinter.Segmentedbutton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
# segmented_button_1.pack(pady=10, padx=10)

# tabview_1 = tkinter.Tabview(master=frame_1, width=300)
# tabview_1.pack(pady=10, padx=10)
# tabview_1.add("CTkTabview")
# tabview_1.add("Tab 2")

app.mainloop()
