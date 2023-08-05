

import turtle
circle=360
numofsides=10
numofobj=100
angle=circle/numofsides
turn=circle/numofobj
side=100
ofset=side*0.1
t=turtle.Pen()
for y in range(0, numofobj):
        for x in range(0, numofsides):
                t.forward(side)
                t.left(angle)
        t.forward(ofset)
        t.left(turn)
	

	
 
