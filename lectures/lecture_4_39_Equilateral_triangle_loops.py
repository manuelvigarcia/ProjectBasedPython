import tkinter as tk
import turtle as t
root = tk.Tk()


t.color('red')

for i in range(0,3):
    t.forward(100)
    t.left(120)

root.mainloop()