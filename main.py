Web VPython 3.2
import random
n=0
boxes = []
curves=[]
helixes=[]
cylinders=[]
cones=[]
rings=[]


while n<50:
    

    curves.append(curve(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)), pos=[vec(- 1, 0, 0),vec(0, 0, - 1), vec(1, 0, 0), vec(0,0,1), vec(-1, 0, 0)]))
    boxes.append(box(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)),color=color.yellow))


    helixes.append(helix(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)), color=color.yellow))
    cylinders.append (cylinder(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10) )))


    cones.append(cone(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))))
    rings.append(ring(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10)), color=color.yellow))
    
    n=n+1

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        for bx in boxes :
            bx.pos.x = bx.pos.x + random.uniform(-1,1)
            bx.pos.y = bx.pos.y + random.uniform(-1,1)
            bx.pos.z = bx.pos.z + random.uniform(-1,1) 
        for cu in curves:
        
        for cu in curves:
            
        for cu in curves:
            
        for cu in curves:
            
        for cu in curves:
            
        
