import random
import tkinter as tk

window = tk.Tk()
canvas =tk.Canvas(window,width=500,height=500,bg='cyan')
canvas.pack()


def generalRect(width,height):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2)

for i in range(4):
    generalRect(350,350)

window.title('my gui')

window.mainloop()