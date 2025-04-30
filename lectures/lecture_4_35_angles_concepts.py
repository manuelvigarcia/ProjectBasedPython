import tkinter as tk
import turtle as t

root = tk.Tk()

#five ways to draw the angles' circle

#somewhat pair by pair of sectors
t.right(90)
t.forward(200)

t.left(90)
t.circle(200, -45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)

t.left(90)
t.circle(200,-45)

input('Press enter to continue . . .')
t.clearscreen()

#Sector by sector
t.right(90)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)

t.forward(200)
t.left(90)
t.circle(200, 45)
t.left(90)
t.forward(200)
t.right(180)


input('Press enter to continue . . .')
t.clearscreen()

# by oposite pairs of sectors
t.forward(200)
t.left(90)
t.circle(200,45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(200)
t.left(45)

t.forward(200)
t.left(90)
t.circle(200,45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(200)
t.left(45)

t.forward(200)
t.left(90)
t.circle(200,45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(200)
t.left(45)

t.forward(200)
t.left(90)
t.circle(200,45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(200)
t.left(45)

input('Press enter to continue . . .')
t.clearscreen()

#four sectors, then circle

t.forward(200)
t.left(180)

t.forward(400)
t.left(90)
t.circle(200,45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-90)

t.left(90)
t.forward(400)
t.left(90)
t.circle(200,-45)
t.left(90)
t.forward(400)
t.left(90)
t.circle(200)

input('Press enter to continue . . .')
t.clearscreen()

#draw each petal
def draw_sectors(radius=100, sectors=4):
    angles = 360 / sectors
    for i in range (0,sectors):
        t.forward(radius)
        t.left(90)
        t.circle(radius,angles)
        t.penup()
        t.setposition(0,0)
        t.right(90)
        t.pendown()


#draw 8 petals
sectors = 8
radius = 200
draw_sectors(radius, sectors)

root.mainloop()