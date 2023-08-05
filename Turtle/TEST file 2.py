
import turtle
circle=360
numofsides=9
numofobj=30
angle=circle/numofsides
turn=circle/numofobj
side=50
ofset=side*5.5
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
        t.forward(ofset)
        t.left(turn)
        t.forward(side)
        t.left(90)
        t.forward(4.5)
        t.left(30)
        t.forward(3.5)
        t.left(30)
        t.forward(2.5)


