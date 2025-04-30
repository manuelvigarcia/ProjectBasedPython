import tkinter as tk
import turtle as t
root = tk.Tk()

t.speed('slow')
t.pencolor('cyan')
t.pensize(10)

t.Screen().bgcolor('red')

def vsnow():
    t.right(30)
    t.forward(60)
    t.backward(60)
    t.left(60)

    t.forward(60)
    t.backward(60)
    t.right(30)


def snow_arm():
    for i in range(0,4):
        t.forward(30)
        vsnow()

    t.backward(120)


def snow_flake():
    for x in range(0,6):
        snow_arm()
        t.right(60)

snow_flake()

root.mainloop()