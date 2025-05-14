import tkinter as tk
import turtle as t
import math

root = tk.Tk()
radius = 200

t.speed('fast')
# t.pencolor('cyan')
# t.pensize(10)
# t.Screen().bgcolor('red')

def draw_poligon(sides=3):
    if sides > 2:
        inner_angle=360/sides
        print("inner angle: " + str(inner_angle))
        outer_angle=180-inner_angle
        print("Outer angle: " + str(outer_angle))
        #math.cos() takes degrees in radians=degrees*pi/180
        interim = 2*(radius**2)
        side_length = math.sqrt(interim - interim*math.cos(inner_angle*math.pi/180))
        print("Side length" + str(side_length))
        t.penup()
        t.left(90)
        t.forward(radius)
        t.pendown()
        t.left(90)
        t.circle(radius)
        t.left((180 - outer_angle)/2)
        for i in range(sides):
            t.forward(side_length)
            t.left(180 - outer_angle)

sides = 3
while sides > 2:
    sides=int(input("How many sides? "))
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.pendown()
    t.clear()
    draw_poligon(sides)

t.clearscreen()

root.mainloop()