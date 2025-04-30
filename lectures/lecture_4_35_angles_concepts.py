import tkinter as tk
import turtle as t

root = tk.Tk()

#four ways to draw the angles' circle

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




"""

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

"""
"""
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
"""

"""
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
"""
root.mainloop()