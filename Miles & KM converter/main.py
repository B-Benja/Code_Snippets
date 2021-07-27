# Miles & kilometer converter

import tkinter

window = tkinter.Tk()
window.title("Mile/KM Converter")
window.minsize(width=200, height=100)

CONSTANT = 1.609347218694

#  based on the radio button input, either divide or multiply by 1.609
def calculate():
    if radio_state.get() == 1:
        user_input = entry.get()
        converted = round(float(user_input) * CONSTANT, 2)
        label_entry = tkinter.Label(text=converted)
        label_entry.grid(column=1, row=3)
    else:
        user_input = entry.get()
        converted = round(float(user_input) / CONSTANT, 2)
        label_entry = tkinter.Label(text=converted)
        label_entry.grid(column=1, row=3)


# radiobutton to decide between km or mile input
def km_layout():
    label_entry = tkinter.Label(text="KM")
    label_entry.grid(column=2, row=2)
    label_km = tkinter.Label(text="Miles")
    label_km.grid(column=2, row=3)


def mile_layout():
    label_entry = tkinter.Label(text="Miles")
    label_entry.grid(column=2, row=2)
    label_miles = tkinter.Label(text="KM")
    label_miles.grid(column=2, row=3)


# basic setup which is necessary for both KM and miles
radio_state = tkinter.IntVar()
radio_state.set(1)
radiobutton1 = tkinter.Radiobutton(text="Mile to KM", value=1, variable=radio_state, command=mile_layout)
radiobutton2 = tkinter.Radiobutton(text="KM to Mile", value=2, variable=radio_state, command=km_layout)
radiobutton1.grid(column=1, row=0)
radiobutton2.grid(column=1, row=1)

entry = tkinter.Entry(width=20)
entry.grid(column=1, row=2)

label_results = tkinter.Label(text="is equal to")
label_results.grid(column=0, row=3)
mile_layout()

calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=4)


window.mainloop()