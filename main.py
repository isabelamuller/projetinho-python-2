from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = tk.Tk()
root.geometry('495x450')
root.title('guess the flag')
Label(root, text='can you guess these five european flags?', font='courier 20 bold').grid()
Label(root, text='good luck!', font='courier 15').grid()
# buttonSt = tk.Button(root, text='start', command=france)
# buttonSt.grid()
canvas = Canvas(root, width=300, height=230)
canvas.grid()
img = (Image.open("france.svg.png"))
resized_image = img.resize((300, 205), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(20, 20, anchor=NW, image=new_image)
pais1_var = tk.StringVar()
pais2_var = tk.StringVar()
pais3_var = tk.StringVar()
pais4_var = tk.StringVar()
pais5_var = tk.StringVar()


def france():
    pais = pais1_var.get()

    if pais == "france":
        tk.messagebox.showinfo("congrats!", "congrats! you got it right! :)")


    else:
        tk.messagebox.showerror("oh no!", "try again baby")


def sweden():
    pais = pais2_var.get()

    if pais == "sweden":
        tk.messagebox.showinfo("congrats!", "congrats! you got it right once again! :)")

    else:
        tk.messagebox.showerror("oh no!", "try again baby")


pais_label = tk.Label(root)
pais_entry = tk.Entry(root, textvariable=pais1_var)

pais_label.grid(row=3, column=0)
pais_entry.grid(row=3, column=0)
sub_btn = tk.Button(root, text='submit', command=france)


def ExitApp():
    MsgBox = tk.messagebox.askquestion('exit', 'are you sure?', icon='error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('welcome back')


sub_btn.grid(row=4, column=0)
buttonEg = tk.Button(root, text='exit', command=ExitApp)
buttonEg.grid()
root.mainloop()
