
import turtle
circle=720
numofsides=8
numofobj=100
angle=circle/numofsides
turn=circle/numofobj
side=50
ofset=side*1-2
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(95)
        t.forward(ofset)
        
        
