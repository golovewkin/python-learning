# simple tk usage
from tkinter import *

root = Tk()

root.geometry('600x400+1000+300')

btn = Button(root, text='text')

btn.pack()
root.mainloop()