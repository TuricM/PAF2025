import math as mt
import numpy as np
import matplotlib.pyplot as plt


#def akc(m,r1,r2,G=6.67408e-11):
#    return [-G*(m*(r1[0]-r2[0]))/(np.abs(r1[0]-r2[0])**3), -G*(m*(r1[1]-r2[1]))/(np.abs(r1[1]-r2[1])**3)]
def korak(a1,a2,v1,v2,r1,r2,m1,m2, dt ,G=6.67408e-11):
    d=mt.sqrt((r1[-1][0]-r2[-1][0])**2+(r1[-1][1]-r2[-1][1])**2) #skalar
    a1.append([-G*(m2*(r1[-1][0]-r2[-1][0]))/(d**3), -G*(m2*(r1[-1][1]-r2[-1][1]))/(d**3)]) #a1x,a1y
    a2.append([-G*(m1*(r2[-1][0]-r1[-1][0]))/(d**3), -G*(m1*(r2[-1][1]-r1[-1][1]))/(d**3)]) #a2x,a2y
    #print("a1: %f ... %f | a2: %f ... %f" %(a1[-1][0],a1[-1][1],a2[-1][0],a2[-1][1]))
    v1.append([v1[-1][0]+a1[-1][0]*dt, v1[-1][1]+a1[-1][1]*dt]) #v1x,v1y
    v2.append([v2[-1][0]+a2[-1][0]*dt, v2[-1][1]+a2[-1][1]*dt]) #v2x,v2y
    r1.append([r1[-1][0]+v1[-1][0]*dt, r1[-1][1]+v1[-1][1]*dt]) #r1x,r1y
    r2.append([r2[-1][0]+v2[-1][0]*dt, r2[-1][1]+v2[-1][1]*dt]) #r2x,r2y
    return 0 #liste se mijenjaju u argumentima, return nije bitan
def gibanje(v1_0,v2_0,r1_0,r2_0,m1,m2, dt, t_fin): #dt i t_fin u sekundama
    a1=[]
    a2=[]
    v1=[v1_0]
    v2=[v2_0]
    r1=[r1_0]
    r2=[r2_0]
    t=0
    while t<t_fin:
        korak(a1,a2,v1,v2,r1,r2,m1,m2,dt)
        t+=dt
    plt.plot([el[0] for el in r1], [el[1] for el in r1], color="blue",label="Sunce")
    plt.plot([el[0] for el in r2], [el[1] for el in r2], color="red", label="Zemlja")
    plt.axis('equal') #Da ne ispadne skašeno
    plt.legend()
    plt.title("Sustav Sunca i Zemlje")
    plt.xlabel("x/m")
    plt.ylabel("y/m")
    plt.show()

gibanje([0,0],[0,29783],[0,0],[1.486e11,0],1.989e30,5.974e24,3600,365.242*24*3600) #v_s, v_z, r_s, r_z, m_s, m_z,dt,t_fin=1god