import particle as p
import math as m

p1 = p.Particle(10,45,[0,0])
print(p1.range())
print((2*100*m.cos(45)*m.sin(45))/9.81)