import tkinter as tk
import turtle as t

root = tk.Tk()

#loop over drawing two pairs of (long side, short side)
for i in range(1,3):
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)

#loop over drawing twice the two sides

def draw_side(side):
    t.forward(side)
    t.left(90)

#stop drawing while moving
t.penup()

#position 50 pixels to the left of the center and 50 pixels below the center
t.setposition(-50,-30)

#start drawing again
t.pendown()
sides = [150,90]
for i in range(1,3):
    for j in sides:
        draw_side(j)

root.mainloop()