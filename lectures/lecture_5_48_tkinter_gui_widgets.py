import tkinter as tk
window = tk.Tk()
window.title('my gui')

tk.Label(window,text='Enter text: ').grid(row=0,column=0)

entry=tk.Entry(window,width=20,bg='pink').grid(row=1,column=0)

tk.Checkbutton(window,text='Checkbutton 1').grid(row=3,column=0)
tk.Checkbutton(window,text='Checkbutton 2').grid(row=4,column=0)

tk.Scale(window,from_=0,to=100,orient=tk.HORIZONTAL).grid(row=4,column=1)

tk.Canvas(window,bg='red',width=150,height=100).grid(row=6,column=2)


window.mainloop()