from tkinter import *
import os

root = Tk()

def myClick():
    myLabel = Label(root, text='Look I clicked a Button')
    myLabel.pack()

myButton = Button(root, text='Press to start', padx = 100, pady = 100, command=myClick)
myButton.pack()

root.mainloop()
