import tkinter as tk
window = tk.Tk()
window.title('my button')
button = tk.Button(window, text='Hi',width=40)
button.pack(padx=20,pady=20)

clickNo=0

def onClick(event):
    global clickNo
    clickNo = clickNo+1
    if clickNo == 1:
        button.configure(text="Clicked 1")
    elif clickNo == 2:
        button.configure(text='Clicked 2')
    else:
        button.pack_forget()

button.bind('<ButtonRelease-1>', onClick)

window.mainloop()