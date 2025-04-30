import tkinter as tk
import turtle as t

root = tk.Tk()

def rect(horiz,vert,color="black"):
    t.pendown()
    t.pensize(2)

    t.color(color)
    t.begin_fill()

    for i in range(1,3):
        t.forward(horiz)
        t.right(90)
        t.forward(vert)
        t.right(90)

    t.end_fill()
    t.penup()
    t.speed('fast')

rect(50,25, 'blue')

root.mainloop()