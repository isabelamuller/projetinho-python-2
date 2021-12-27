from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('405x600')
root.title('guess the flag')
Label(root, text='can you guess this european flag?', font='courier 20 bold').grid()
Label(root, text='good luck!', font='courier 15').grid()
pais1_var = tk.StringVar()


def buttonst():
    canvas1 = Canvas(root, width=350, height=233)
    canvas1.grid(row=3, column=0)
    img2 = PhotoImage(file="france.svg.png")
    canvas1.create_image(0, 0, image=img2, anchor=NW)
    canvas1.img2 = img2


buttonst1 = tk.Button(root, text='start', command=buttonst)
buttonst1.grid(row=2, column=0)


def france():
    pais = pais1_var.get()

    if pais == "france":
        tk.messagebox.showinfo("congrats!", "congrats! you got it right! :)")

    else:
        tk.messagebox.showerror("oh no!", "try again baby")


pais_label = tk.Label(root)
pais_entry = tk.Entry(root, textvariable=pais1_var)

pais_label.grid(row=4, column=0)
pais_entry.grid(row=4, column=0)
sub_btn = tk.Button(root, text='submit', command=france)
sub_btn.grid(row=7, column=0)


def buttonnx():
    canvas2 = Canvas(root, width=150, height=150)
    canvas2.grid(row=9, column=0)
    img1 = PhotoImage(file="surprise.png")
    canvas2.create_image(0, 0, image=img1, anchor=NW)
    canvas2.img1 = img1


buttonNt = Button(root, text='surprise', command=buttonnx)
buttonNt.grid(row=8, column=0)


def ExitApp():
    MsgBox = tk.messagebox.askquestion('exit', 'are you sure?', icon='error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('welcome back')


buttonEg = tk.Button(root, text='exit', command=ExitApp)
buttonEg.grid(row=10, column=0)
root.mainloop()
