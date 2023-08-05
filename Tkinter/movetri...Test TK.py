def Right():
    canvas.bind_all('<KeyPress-Up>', movetriangle)
def Left():
    canvas.bind_all('<KeyPress-Down>', movetriangle)
def Down():
    canvas.bind_all('<KeyPress-Left>', movetriangle)
def Up():
    canvas.bind_all('<KeyPress-Right>', movetriangle)
from tkinter import *
tk = Tk()
btn = Button(tk, text="Right", command=Right)
btn.pack()
btn = Button(tk, text="Left", command=Left)
btn.pack()
btn = Button(tk, text="Down", command=Down)
btn.pack()
btn = Button(tk, text="Up", command=Up)
btn.pack()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="blue",
outline="magenta")
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3) 
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Up>', movetriangle)
