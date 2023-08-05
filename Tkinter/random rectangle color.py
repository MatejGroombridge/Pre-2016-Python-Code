from tkinter import *
import random
w = 500
h = 500
tk = Tk()
canvas = Canvas(tk, width=w, height=h)
canvas.pack()
colors = ['red','green','blue','yellow','orange','black','purple',\
          'magenta','pink','lime','white','violet','indigo','cyan','maroon',\
          'peru','gold','wheat','teal','aqua','turquoise','olive','silver',\
          'chartreuse','grey','navy','salmon','coral','tan']
def random_triangle():
    p1 = random.randrange(w)
    p2 = random.randrange(h)
    p3 = random.randrange(w)
    p4 = random.randrange(h)
##    p5 = random.randrange(w)
##    p6 = random.randrange(h)
    color = random.choice(colors)
    canvas.create_rectangle(p1, p2, p3, p4, fill=color, outline=color)
for x in range(0, 10000):
 random_triangle()
