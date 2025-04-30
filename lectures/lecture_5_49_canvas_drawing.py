import tkinter as tk
window = tk.Tk()

canvas =tk.Canvas(window,width=500,height=500,bg='pink')
canvas.pack()
canvas.create_rectangle(10,10,50,50)
canvas.create_rectangle(20,20,300,100)
canvas.create_rectangle(20,20,100,300)




window.title('my gui')






window.mainloop()