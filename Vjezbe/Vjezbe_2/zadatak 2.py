import numpy as np
import matplotlib.pyplot as plt
import math as m

v_0= float(input("Unesi pocetnu brzinu[m/s]: "))
fi= float(input("Unesi kut otklona[°]: "))
t_uk=10
dt=0.001
a_x=0
a_y=-9.81
x_0=0
y_0=0
v_x=[v_0*m.cos(m.radians(fi))]
v_y=[v_0*m.sin(m.radians(fi))]
x=[x_0]
y=[y_0]
t=[0]
s=0
for i in np.arange(0,t_uk,dt):
    if y[s]<=0 and i!=0:
        break
    v_x.append(v_x[s]+a_x*dt)
    v_y.append(v_y[s]+a_y*dt)
    x.append(x[s]+v_x[s+1]*dt)
    y.append(y[s]+v_y[s+1]*dt)
    t.append(t[s]+dt)
    s+=1
    
fig, ax = plt.subplots(1,3)

ax[0].plot(x,y)
ax[0].set_xlabel("x [m]")
ax[0].set_ylabel("y [m]")


ax[1].plot(t,x)
ax[1].set_xlabel("t [s]")
ax[1].set_ylabel("x [m]")

ax[2].plot(t,y)
ax[2].set_xlabel("t [s]")
ax[2].set_ylabel("y [m]")
plt.tight_layout()
plt.show()