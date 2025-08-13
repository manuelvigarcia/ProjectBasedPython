import sys; print(sys.executable)
import os; print(os.getcwd())
import sys; print(sys.path)
sys.path.append("C:\\Program Files\\Python313\\Lib\\site-packages")
import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()
window.mainloop()
