from graphics import *
win = GraphWin()
lefteye = Circle(Point(80, 50), 5)
lefteye.setFill('yellow')
lefteye.setOutline('red')
win.draw(lefteye)
righteye = Circle(Point(100, 50), 5)
righteye.setFill('yellow')
righteye.setOutline('red')
win.draw(righteye)