
import turtle
circle=360
numofsides=20
numofobj=30
angle=circle/numofsides
turn=circle/numofobj
side=10
ofset=side*10
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
        t.forward(ofset)
        t.left(turn)
        t.forward(side)
        t.left(90)
        t.forward(9.5)
        t.left(30)
        



