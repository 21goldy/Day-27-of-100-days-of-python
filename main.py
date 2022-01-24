from logging import root
from tkinter import *

COLOR = "#00EEEE"
FONT_NAME = "Courier"

# window
window = Tk()
window.title("Miles to Kms converter")
window.minsize(width=100, height=100)
window.config(bg=COLOR)

# window label
window_label = Label(text="Convert - 'Miles to Kms'", font=("Courier", 15, "bold"), bg=COLOR)
window_label.grid(row=0, column=1)
window_label.config(pady=20)

# miles_label
miles_label = Label(text="Miles->", font=("Courier", 15), bg=COLOR)
miles_label.grid(row=1, column=0)

# kms_label
kms_label = Label(text="Kms->", font=("Courier", 15), bg=COLOR)
kms_label.grid(row=4, column=0)
kms_label.config(padx=20, pady=20)

# calculated_value label
calculated_value = Label(text="", font=("Courier", 15, "bold"), bg=COLOR)
calculated_value.grid(row=4, column=1)
calculated_value.config(padx=20, pady=20)

# input window
input_window = Entry()
input_window.grid(row=1, column=1)


# calculation part
def converter():
    miles = int(input_window.get())
    converted = round(miles * 1.609344)
    calculated_value.config(text=f"'{converted} kms'", bg=COLOR)
    print(converted)


# calculate button
calculate_button = Button(text="calculate", font=("Courier", 10, "bold"), bg="#F0F8FF", command=converter)
calculate_button.grid(row=2, column=1)


window.mainloop()
