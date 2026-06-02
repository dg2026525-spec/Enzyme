Web VPython 3.2
import random
n=0
bp=0
hc=0
cr=0

boxes = []
helixes=[]
cylinders=[]
cones=[]
rings=[]
pyramids=[]

while n<100:
    
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

        for bx in boxes:
            for py in pyramids:
                if py.opacity>0:
                    if abs(bx.pos.x-py.pos.x) + abs(bx.pos.y-py.pos.y) + abs(bx.pos.z-py.pos.z) < 2:
                        py.opacity=0
                        pyramids.remove(py)
                    
                        bp=bp+1
                    
        for he in helixes :
            for cy in cylinders :
                if cy.opacity>0:
                    if abs(he.pos.x-cy.pos.x) + abs(he.pos.y-cy.pos.y) + abs(he.pos.z-cy.pos.z) < 2:
                        cy.opacity=0
                        cylinders.remove(cy)
                    
                        hc=hc+1


        for co in cones :
            for ri in rings :
                if co.opacity>0:
                    if abs(co.pos.x-ri.pos.x) + abs(co.pos.y-ri.pos.y) + abs(co.pos.z-ri.pos.z) < 2:
                        co.opacity=0
                        cones.remove(co)
                    
                        cr=cr+1            
                    
        

    if 'a' in k :
        print("효소1:", bp)
        print("효소2:", hc)
        print("효소3:", cr)































 
