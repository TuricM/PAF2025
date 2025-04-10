import particle as p
import math as m

p1 = p.Particle(10,45,[0,0])
#print(p1.plot_trajectory())
print((2*100*m.cos(m.radians(45))*m.sin(m.radians(45)))/9.81)
print(p1.range(0.01))