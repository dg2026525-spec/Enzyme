
Web VPython 3.2
import random

box(size=vec(100,100,100), opacity=0.1, color=color.cyan)

cu=curve(pos=[vec(- 1, 0, 0),vec(0, 0, - 1), vec(1, 0, 0), vec(0,0,1), vec(-1, 0, 0)])
b=box(pos=vec(random.uniform(-5,5),0,random.uniform(-5,5)),color=color.yellow)


h= helix(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)), color=color.yellow)
cy=cylinder(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)))


cn=cone(pos=vec(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)))
r=ring(pos=vec(random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)), color=color.yellow)






while True : 
    rate(100)
    k = keysdown()
    if ' ' in k :
        
