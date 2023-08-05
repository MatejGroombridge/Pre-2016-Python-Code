

def New():
    btn2 = Button(t, text="click me too", command=New2)
    btn2.pack()
    

def New2():
    canvas = Canvas(t, width=400, height=450)
    canvas.pack()
    canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='Red', outline='Yellow')

    
from tkinter import *
t = Tk()
btn = Button(t, text="click me", command=New)
btn.pack()
 
