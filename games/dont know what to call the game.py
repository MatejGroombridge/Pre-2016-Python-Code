from tkinter import *
import random
import time

class RedBall:
    def __init__(self, canvas, BlueBall, color, block):
        self.canvas = canvas
        self.BlueBall = BlueBall
        self.block = block
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 
