import math as m
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,fi,poc): #poc oznacava pocetne kordinate kao listu [x0,y0]
        self.v0=v0
        self.fi=m.radians(fi)
        self.r=[poc[0],poc[1]]
        self.v=[self.v0*m.cos(self.fi),self.v0*m.sin(self.fi)]
        self.g=-9.81
        self.pocetni=[v0,m.radians(fi),poc]
    def reset(self):
        self.v0=self.pocetni[0]
        self.fi=self.pocetni[1]
        self.r=[self.pocetni[2][0],self.pocetni[2][1]]
        self.v=[self.v0*m.cos(self.fi),self.v0*m.sin(self.fi)]
    def __move(self, dt):
        self.v[1] = self.v[1]+ self.g*dt
        self.r[0]=self.r[0]+self.v[0]*dt
        self.r[1]=self.r[1]+self.v[1]*dt
        #print(self.r[0])
    def range(self, dt): #Nova izmjena - dodan argument dt
        while self.r[1]>=0:
            self.__move(dt)
        D=self.r[0]
        self.reset()
        return D
    def plot_trajectory(self):
        x=[]
        y=[]
        while self.r[1]>=0:
            x.append(self.r[0])
            y.append(self.r[1])
            self.__move(0.01)
        plt.plot(x,y)
        plt.show()
        self.reset()