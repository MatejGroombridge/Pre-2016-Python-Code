
import turtle
circle=720
numofsides=1
numofobj=10
angle=circle/numofsides
turn=circle/numofobj
side=50
ofset=side*1
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
                t.forward(51)
                t.left(90)
                t.forward(52)
        t.forward(ofset)
        t.left(turn)
        t.forward(side)
        
