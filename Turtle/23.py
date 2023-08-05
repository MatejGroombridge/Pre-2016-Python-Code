
import turtle
circle=360
numofsides=100
numofobj=100
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
                t.left(95)
                t.forward(52)
        t.forward(ofset)
        t.left(90)
        t.forward(side)
        t.right(90)
        
        
