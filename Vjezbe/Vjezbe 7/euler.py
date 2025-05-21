import numpy as np
import math as mt
import matplotlib.pyplot as plt


class Projectile:
    def __init__(self, m, v, fi, r_0, ro, C_d, A):
        self.m = m
        self.ro=ro
        self.C_d=C_d
        self.A=A
        self.fi=mt.radians(fi)
        self.v=[[v*mt.cos(self.fi), v*mt.sin(self.fi)]]
        self.v_0=v
        self.r=[r_0]
        self.r_0=r_0
        self.a=[]

    def reset(self):
         self.v=[[self.v_0*mt.cos(self.fi), self.v_0*mt.sin(self.fi)]]
         self.r=[self.r_0]
         self.a=[]

    def akc(self, ro, C_d, A, m, v, g=-9.81):
        return [-np.sign(v[0])*(ro*C_d*A)/(2*m)*(v[0]**2), g-np.sign(v[1])*(ro*C_d*A)/(2*m)*(v[1]**2)]
    
    def Euler_korak(self, dt):
        self.a.append(self.akc(self.ro, self.C_d, self.A, self.m, self.v[-1]))
        self.v.append([self.v[-1][0]+self.a[-1][0]*dt, self.v[-1][1]+self.a[-1][1]*dt])
        self.r.append([self.r[-1][0]+self.v[-1][0]*dt, self.r[-1][1]+self.v[-1][1]*dt])
    
    def RK_korak(self, dt):
        k1v= self.akc(self.ro, self.C_d, self.A, self.m, self.v[-1])
        k1r= [self.v[-1][0]*dt, self.v[-1][1]*dt]
        k2v=self.akc(self.ro, self.C_d, self.A, self.m, [self.v[-1][0]+k1v[0]*dt/2, self.v[-1][1]+k1v[1]*dt/2])
        k2r=[(self.v[-1][0]+(k1v[0]*dt)/2)*dt,( self.v[-1][1]+(k1v[1]*dt)/2)*dt]
        k3v=self.akc(self.ro, self.C_d, self.A, self.m, [self.v[-1][0]+k2v[0]*dt/2, self.v[-1][1]+k2v[1]*dt/2])
        k3r=[(self.v[-1][0]+(k2v[0]*dt)/2)*dt,( self.v[-1][1]+(k2v[1]*dt)/2)*dt]
        k4v=self.akc(self.ro, self.C_d, self.A, self.m, [self.v[-1][0]+k3v[0]*dt, self.v[-1][1]+k3v[1]*dt])
        k4r=[(self.v[-1][0]+(k3v[0]*dt))*dt,( self.v[-1][1]+(k3v[1]*dt))*dt]

        self.v.append([self.v[-1][0]+(1/6)*dt*(k1v[0]+2*k2v[0]+2*k3v[0]+k4v[0]), self.v[-1][1]+(1/6)*dt*(k1v[1]+2*k2v[1]+2*k3v[1]+k4v[1])])
        self.r.append([self.r[-1][0]+(1/6)*(k1r[0]+2*k2r[0]+2*k3r[0]+k4r[0]), self.r[-1][1]+(1/6)*(k1r[1]+2*k2r[1]+2*k3r[1]+k4r[1])])
        print(self.v[-1])
    def gibanje_euler(self):
        self.reset()
        while self.v[-1][1]>=0 or self.r[-1][1]>0:
            self.Euler_korak(0.01)
        plt.plot([el[0] for el in self.r], [el[1] for el in self.r], color = "red")
        #plt.show()
        
    def gibanje_RK(self):
        self.reset()
        while self.v[-1][1]>=0 or self.r[-1][1]>0:
            self.RK_korak(0.01)
        plt.plot([el[0] for el in self.r], [el[1] for el in self.r], color="blue")
        #plt.show()

p1 = Projectile(1,10,45,[0,0],1.225,0.5,1)
p1.gibanje_euler()
p1.gibanje_RK()
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.legend(["Eulerova metoda", "Runge-Kutta metoda"])
plt.show()