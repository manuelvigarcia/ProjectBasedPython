import tkinter as tk
window = tk.Tk()
window.title('my button')
button = tk.Button(window, text='Hi',width=40)
button.pack(padx=20,pady=20)
window.mainloop()