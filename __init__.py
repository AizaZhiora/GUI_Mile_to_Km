from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def calc():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 3)
    number_label.config(text=km)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equals to')
equal_label.grid(column=0, row=1)

number_label = Label(text='0')
number_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=calc)
button.grid(column=1, row=2)

window.mainloop()
