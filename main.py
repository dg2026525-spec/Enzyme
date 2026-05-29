Web VPython 3.2
import random
n=0
boxes = []
helixes=[]
cylinders=[]
cones=[]
rings=[]
pyramids=[]

while n<50:
    
    pyramids.append(pyramid(pos=vec(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))))
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
                       
        for py in pyramids :
            py.pos.x = py.pos.x + random.uniform(-1,1)
            py.pos.y = py.pos.y + random.uniform(-1,1)
            py.pos.z = py.pos.z + random.uniform(-1,1) 
        
        for he in helixes :
            he.pos.x = he.pos.x + random.uniform(-1,1)
            he.pos.y = he.pos.y + random.uniform(-1,1)
            he.pos.z = he.pos.z + random.uniform(-1,1) 
        
        for cy in cylinders :
            cy.pos.x = cy.pos.x + random.uniform(-1,1)
            cy.pos.y = cy.pos.y + random.uniform(-1,1)
            cy.pos.z = cy.pos.z + random.uniform(-1,1)         
            
        for co in cones :
            co.pos.x = co.pos.x + random.uniform(-1,1)
            co.pos.y = co.pos.y + random.uniform(-1,1)
            co.pos.z = co.pos.z + random.uniform(-1,1)

        for ri in rings :
            ri.pos.x = ri.pos.x + random.uniform(-1,1)
            ri.pos.y = ri.pos.y + random.uniform(-1,1)
            ri.pos.z = ri.pos.z + random.uniform(-1,1) 
        
 
