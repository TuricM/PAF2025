import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, v_0, x_0, k, m):
        self.x_0=x_0
        self.v_0=v_0
        self.x= [x_0]
        self.v= [v_0]
        self.a= [-k/m*x_0]
        self.k= k
        self.m= m
        self.t= [0]
    def oscillate(self, dt):
        self.reset()
        br=0
        while br<=4:
            self.v.append(self.v[-1]+self.a[-1]*dt)
            self.x.append(self.x[-1]+self.v[-1]*dt)
            
            self.a.append(-self.k/self.m*self.x[-1])
            self.t.append(self.t[-1]+dt)
            if self.x[-2]<=0 and self.x[-1]>=0 or self.x[-2]>=0 and self.x[-1]<0:
                br+=1
    def plot_trajectory(self):
        fig, ax = plt.subplots(1,3)

        ax[0].plot(self.t,self.x)
        ax[0].set_xlabel("t [s]")
        ax[0].set_ylabel("x [m]")


        ax[1].plot(self.t,self.v)
        ax[1].set_xlabel("t [s]")
        ax[1].set_ylabel("v [m/s]")

        ax[2].plot(self.t,self.a)
        ax[2].set_xlabel("t [s]")
        ax[2].set_ylabel("a [m/s^2]")
        plt.tight_layout()
        plt.show()
    def reset(self):
        self.x= [self.x_0]
        self.v= [self.v_0]
        self.a= [-self.k/self.m*self.x_0]
        self.t= [0]
    def period(self, dt):
        self.reset()
        br=0
        while br<=2:
            self.v.append(self.v[-1]+self.a[-1]*dt)
            self.x.append(self.x[-1]+self.v[-1]*dt)
            
            self.a.append(-self.k/self.m*self.x[-1])
            self.t.append(self.t[-1]+dt)
            if self.x[-2]<=0 and self.x[-1]>=0 or self.x[-2]>=0 and self.x[-1]<0:
                br+=1
        return self.t[-1]