import math as m
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v0,fi,poc): #poc oznacava pocetne kordinate kao listu [x0,y0]
        self.v0=v0
        self.fi=m.radians(fi)
        self.r=[poc[0],poc[1]]
        self.v=[self.v0*m.cos(self.fi),self.v0*m.sin(self.fi)]
        self.g=-9.81
    #def reset(self):
     #   self.v0=v0
     #   self.fi=fi
     #   self.r=[poc[0],poc[1]]
     #   self.v=[self.v0*m.cos(self.fi),self.v0*m.sin(self.fi)]
     #   self.g=-9.81
    def __move(self, dt):
        self.v[1] = self.v[1]+ self.g*dt
        self.r[0]=self.r[0]+self.v[0]*dt
        self.r[1]=self.r[1]+self.v[1]*dt
    def range(self):
        while self.r[1]>=0:
            self.__move(0.0001)
            #print("%g    %g" % (self.r[0], self.r[1]))
        D=self.r[0]
        # self.reset()
        return D
    def plot_trajectory(self):
        x=[]
        y=[]
        while self.r[1]>0:
            x.append(self.r[0])
            y.append(self.r[1])
            self.__move(0.01)
        plt.plot(x,y)
        plt.show()