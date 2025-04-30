from math import *
from tkinter import *

def evaluate(event):
    res.configure(text='Answer: ' + str(eval(entry.get())))


w = Tk()
w.title("Temperature Converter")

fahrlabel = Label(w,text='Farenheit')
fahrlabel.grid(row=0,column=0,padx=5,pady=5,sticky=E)

celllabel = Label(w,text='Celsius')
celllabel.grid(row=1,column=0,padx=5,pady=5,sticky=E)

kellabel = Label(w,text='Kelvin')
kellabel.grid(row=2,column=0,padx=5,pady=5,sticky=E)

fbtext=StringVar()
fbtext.set('')
fahrbox=Entry(w,textvariable=fbtext)
fahrbox.grid(row=0,column=1,padx=5,pady=5)

cbtext=StringVar()
cbtext.set('')
celbox=Entry(w,textvariable=cbtext)
celbox.grid(row=1,column=1,padx=5,pady=5)

kbtext=StringVar()
kbtext.set('')
kelbox=Entry(w,textvariable=kbtext)
kelbox.grid(row=2,column=1,padx=5,pady=5)


exitbutton = Button(w,text='Exit',command=quit)
exitbutton.grid(row=3,column=0,padx=5,pady=5,sticky=N+S+E+W,columnspan=3)

w.mainloop()