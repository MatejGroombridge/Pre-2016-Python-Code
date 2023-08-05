from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        starts = [-3, -2, -1, 1, 2, 3]
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.x, self.y)
        self.y = 3
        self.y = -3
        self.x = 3
        self.x = -3


    def turn_left(self, evt):
        self.x = -2
         
    def turn_right(self, evt):
        self.x = 2
        

    def start_game(self, evt):
        self.started = True
        
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow')

while 1:
    if ball.hit_bottom == False:
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.015)
