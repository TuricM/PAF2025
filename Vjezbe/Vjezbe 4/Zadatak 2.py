import math as m
import numpy as np
import matplotlib.pyplot as plt
import particle as prt
'''def domet(dt):
    v0=10 #m/s
    fi = 60 #°
    g = -9.81 #m/s^2
    v = [v0*m.cos(m.radians(fi)), v0*m.sin(m.radians(fi))] #[v_x,v_y]
    r=[0,0]  #[x,y]
    while r[1] >= 0:
        v[1] = v[1] + g*dt
        r[0] = r[0] + v[0]*dt
        r[1] = r[1] + v[1]*dt
        print(r[0])
    return r[0]






print("dt= 0.08 : %f      %f"%(domet(0.08), D))
print("----------------------")
print("dt= 0.0803 : %f      %f"%(domet(0.0803), D))
'''
D = (100/9.81)*m.sin(m.radians(2*60)) # ANALITICKI v0^2/g * sin(2fi)
p = prt.Particle(10,60,[0,0])
raz = np.linspace(0.0001,0.1,1000)
y = []
'''print("%f,%f     %f,%f" %(p.v[0],p.v[1], p.r[0],p.r[1]))
print(p.range(0.01))
print("%f,%f     %f,%f" %(p.v[0],p.v[1], p.r[0],p.r[1]))'''
for i in raz:
    #print("%f  ...   %f" %(i, p.range(i)))
    y.append(abs(p.range(i)-D)/D*100) #greska u %
plt.title("Relativna pogreška")
plt.xlabel("dt/s")
plt.ylabel("%")
plt.plot(raz, y)
plt.show()
"""Graf nije isti kao primjer u predavanju. 
Pokušao sam na dva načina, prvo bez klasa i funkcija, kao u vježbi 2, a onda ponovno modificiranjem modula particle.py.
Rezultat je bio isti, pa sam pokušao u C-u i napravio graf u gnuplotu, ali je rezultat ponovno isti."""