import numpy as np
import matplotlib.pyplot as plt

F = float(input("Unesi iznos sile[N]: "))
m = float(input("Unesi masu[kg]: "))
t_uk = 10
dt = 0.1
v0=0
x0=0
a_0 = F/m
a=[a_0]
v=[v0]
x=[x0]
t=[0]
s=0
for i in np.arange(0,t_uk,dt):
    a.append(a_0)
    v.append(v[s]+a[s]*dt)
    x.append(x[s]+v[s+1]*dt)
    t.append(t[s]+dt)
    s+=1


fig, ax = plt.subplots(1,3)

ax[0].scatter(t,x)
ax[0].set_xlabel("t [s]")
ax[0].set_ylabel("x [m]")


ax[1].plot(t,v)
ax[1].set_xlabel("t [s]")
ax[1].set_ylabel("v [m/s]")

ax[2].plot(t,a)
ax[2].set_xlabel("t [s]")
ax[2].set_ylabel("a [m^2/s]")
plt.tight_layout()
plt.show()
