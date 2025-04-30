from math import *
from tkinter import *

def evaluate(event):
    res.configure(text='Answer: ' + str(eval(entry.get())))


window = Tk()
Label(window,text="Your expression: ").pack()

entry = Entry(window)
entry.bind('<Return>',evaluate)
entry.pack()


res=Label(window)
res.pack()

window.mainloop()