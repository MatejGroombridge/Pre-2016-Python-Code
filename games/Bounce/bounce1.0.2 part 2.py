from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, paddle2, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.paddle2 = paddle2
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

        
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Ball2:
    def __init__(self, canvas, paddle, paddle2, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.paddle2 = paddle2
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 225, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

        
    def hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                self.x += self.paddle2.x
                self.score.hit()
                return True
        return False

    
    def draw2(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle2(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)
 
    def draw(self):
      self.canvas.move(self.id, self.x, 0)
      pos = self.canvas.coords(self.id)
      if pos[0] <= 0:
          self.x = 0
      elif pos[2] >= self.canvas_width:
          self.x = 0

    def turn_left(self, evt):
        self.x = -2
         
    def turn_right(self, evt):
        self.x = 2
        

    def start_game(self, evt):
        self.started = True

class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 300, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-1>', self.turn_left3)
        self.canvas.bind_all('<KeyPress-2>', self.turn_right3)
 
    def draw3(self):
      self.canvas.move(self.id, self.x, 0)
      pos = self.canvas.coords(self.id)
      if pos[0] <= 0:
          self.x = 0
      elif pos[2] >= self.canvas_width:
          self.x = 0

    def turn_left3(self, evt):
        self.x = -2
         
    def turn_right3(self, evt):
        self.x = 2
        

    def start_game3(self, evt):
        self.started = True

        
class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, \
                fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'green')
ball = Ball(canvas, paddle, score, 'aqua')
ball2 = Ball2(canvas, paddle, score, 'yellow')
paddle2 = Paddle2(canvas, 'purple')
game_over_text = canvas.create_text(250, 200, text='GAME OVER', fill='red', \
        state='hidden')

while 1:
    if ball.hit_bottom == False and paddle.started == True:
        ball.draw()
        paddle.draw()
        ball2.draw2()
        paddle2.draw3()
    if ball.hit_bottom == True:
        time.sleep(1)
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.012)
