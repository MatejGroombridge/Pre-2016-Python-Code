
import turtle
circle=720
numofsides=12
numofobj=5
angle=circle/numofsides
turn=circle/numofobj
side=50
ofset=side*1.5
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
                t.forward(51)
                t.left(90)
                t.forward(52)
                t.left(90)
                t.forward(53)
        t.forward(ofset)
        t.left(turn)
        t.forward(side)
        
