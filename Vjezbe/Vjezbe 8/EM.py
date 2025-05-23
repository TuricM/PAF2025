import math as m
import numpy as np
import matplotlib.pyplot as plt


def akc(v,q,m,E,B):
    a = [0,0,0]
    a[0] = (q/m)*(E[0]+v[1]*B[2]-(v[2]*B[1]))
    a[1] = (q/m)*(E[1]-(v[0]*B[2]-(v[2]*B[0])))
    a[2] = (q/m)*(E[2]+v[0]*B[1]-(v[1]*B[0]))
    #print("akceleracija: %f | %f | %f"%(a[0], a[1],a[2]))
    #print((q/m)*(E[0]+v[1]*B[2]-(v[2]*B[1])))
    return a

def korak(v,q,m,E,B,r, dt, t=0):
    a = akc(v,q,m,E,B)
    v_n = [v[0]+ a[0]*dt, v[1]+ a[1]*dt, v[2]+ a[2]*dt]
    r_n = [r[0]+v[0]*dt, r[1]+v[1]*dt, r[2]+v[2]*dt]
    t+=dt
    return v_n, r_n, t
v_0=[1,2,1]
r_0=[0,0,0]
E=[0,0,0]
B=[0,0,1]
q=-1 #"Elektron"
m=1
t=0
dt=0.01
v=[v_0]
r=[r_0]
while t<10:
    v_n, r_n, t = korak(v[-1],q,m,E,B,r[-1],dt,t)
    v.append(v_n)
    r.append(r_n)
    #print(v[-1])
ax = plt.axes(projection='3d')
ax.scatter3D([el[0] for el in r],[el[1] for el in r],[el[2] for el in r], lw=0.2)

v_0=[1,2,1]
r_0=[0,0,0]
E=[0,0,0]
B=[0,0,1]
q=1 #Pozitron
m=1
t=0
dt=0.01
v=[v_0]
r=[r_0]
while t<10:
    v_n, r_n, t = korak(v[-1],q,m,E,B,r[-1],dt,t)
    v.append(v_n)
    r.append(r_n)
    #print(v[-1])
#ax = plt.axes(projection='3d')
ax.scatter3D([el[0] for el in r],[el[1] for el in r],[el[2] for el in r], lw=0.2)
ax.set_title("Gibanje elektrona i pozitrona u homogenom magnetskom polju: v=(1,2,1) E=0 B=(0,0,1)")
ax.legend(["Elektron", "Pozitron"])
ax.set_xlabel("x/m")
ax.set_ylabel("y/m")
ax.set_zlabel("z/m")
plt.show()