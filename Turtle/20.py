
import turtle
circle=720
numofsides=4
numofobj=4
angle=circle/numofsides
turn=circle/numofobj
side=100
ofset=side*1
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
                t.forward(101)
                t.left(90)
                t.forward(102)
                t.left(90)
                t.forward(103)
                t.right(90)
                t.forward(104)
                t.right(90)
                t.forward(105)
                t.right(90)
        t.forward(ofset)
        
        
