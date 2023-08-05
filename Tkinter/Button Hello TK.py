

def hello():
    print('hello there')

	
from tkinter import *
t = Tk()
btn = Button(t, text="click me", command=hello)
btn.pack()
 
