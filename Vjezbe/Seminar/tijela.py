import numpy as np
import math as mt
import matplotlib.pyplot as plt
from matplotlib import animation
#import ipython as ip

class Tijelo:
    objekti=[] #Lista koja sadržava sva tijela
    lines=[]
    fig, ax = plt.subplots(figsize=(12, 6))
        
    #line, = ax.plot([],[])
    def __init__(self,m,r_0,v_0, ime, d_linije=2, auto_dodaj=True):
        self.ime=ime #Samo za legendu
        self.m=m
        self.lw = d_linije
        self.r=[r_0]
        self.v=[v_0]
        self.a=[0,0]
        self.flag = 0 #Oznacava nestanak objekta (u ovom slucaju sudar)
        Tijelo.objekti.append(self) #Dodamo tijelo u listu
    
    def akceleracija(self, G=6.67408e-11):
        # m*a=G mM/r**2
        # a_x = a*cosfi = a* x/d
        # a_y = a* y/d
        if self.flag == 1:
            return
        self.a=[0,0]
        for obj in Tijelo.objekti:
            if obj != self and obj.flag == 0: #Da se ne računa utjecaj objekta samog na sebe, bude 0 udaljenost
                d = [obj.r[-1][0]-self.r[-1][0], obj.r[-1][1]-self.r[-1][1]] # vektor udaljenosti od tijela do nekog objekta
                d_iznos= mt.sqrt(d[0]**2+d[1]**2)
                #print(obj.r)
                self.a=[self.a[0]+G*obj.m/(d_iznos**2)*(d[0]/d_iznos), self.a[1]+G*obj.m/(d_iznos**2)*(d[1]/d_iznos)] #pridonos akceleracije jednog objekta na tijelo
                #Unutar jedne kalkulacije akceleracije krece se od 0, pa se svaku iteraciju zbraja doprinos svakog objekta
        return 0
    
    def __korak(d_sudar,t,dt):
        #SUDAR
        dodavanje=[]
        brisanje=[]
        for obj in Tijelo.objekti:
            for meta in Tijelo.objekti:
                if obj != meta and ((obj.r[-1][0]-meta.r[-1][0])**2+(obj.r[-1][1]-meta.r[-1][1])**2)<d_sudar**2 and meta.flag==0 and obj.flag==0:
                    #novo_tijelo = Tijelo(obj.m+meta.m,obj.r[-1],[obj.v[-1][0]+meta.v[-1][0], obj.v[-1][1]+meta.v[-1][1]],obj.ime+" + "+meta.ime)
                    #Napravimo novi objekt ; neelasticni sudar, mase i brzine se zbroje, brisemo obj i metu
                    print("PROJEKTIL: %s META: %s" %(obj.ime, meta.ime))
                    obj.flag=1
                    meta.flag=1
                    #v = p_uk/m_uk
                    #r = centar mase
                    dodavanje.append([obj.m+meta.m,
                                    [(obj.m*obj.r[-1][0]+meta.m*meta.r[-1][0])/(obj.m+meta.m),(obj.m*obj.r[-1][1]+meta.m*meta.r[-1][1])/(obj.m+meta.m)],
                                     [(obj.m*obj.v[-1][0]+meta.m*meta.v[-1][0])/(obj.m+meta.m), (obj.m*obj.v[-1][1]+meta.m*meta.v[-1][1])/(obj.m+meta.m)],
                                     obj.ime+" + "+meta.ime])
        for el in dodavanje:
            novo_tijelo= Tijelo(el[0],[float("nan"), float("nan")], [float("nan"), float("nan")],el[3])
            for i in np.arange(0,t-dt,dt):
                novo_tijelo.v.append([float("nan"), float("nan")])
                novo_tijelo.r.append([float("nan"), float("nan")])
            novo_tijelo.v.append(el[2])
            novo_tijelo.r.append(el[1])
            

        for obj in Tijelo.objekti:
            if obj.flag == 0:
                obj.akceleracija()
            else:
                obj.a=[float("nan"),float("nan")]
        for obj in Tijelo.objekti:
            if obj.flag == 0:
                obj.v.append([obj.v[-1][0]+obj.a[0]*dt, obj.v[-1][1]+obj.a[1]*dt])
            else:
                obj.v.append([float("nan"), float("nan")])
        for obj in Tijelo.objekti:
            if obj.flag == 0:
                obj.r.append([obj.r[-1][0]+obj.v[-1][0]*dt, obj.r[-1][1]+obj.v[-1][1]*dt])
            else:
                obj.r.append([float("nan"), float("nan")])

    

    def gibanje(t_fin,dt):
        
        """for i in range(len(Tijelo.objekti)): #Za svaki objekt inicijaliziramo liniju
            line, = ax.plot([],[])
            #Tijelo.lines.append(line,) Ne valja?"""
        
        t=0
        while t<t_fin:
            Tijelo.__korak(1e10,t,dt)

            t+=dt
        #for obj in Tijelo.objekti:
        #    plt.plot([el[0] for el in obj.r],[el[1] for el in obj.r], label=obj.ime)
        #plt.axis('equal')
        crtaj_svakih_n=3 #Izgleda optimalno, crta svaku 3. tocku
        frames = range(0, len(Tijelo.objekti[0].r), crtaj_svakih_n)
        anim = animation.FuncAnimation(Tijelo.fig,Tijelo.crtanje,init_func=Tijelo.init, frames=frames, interval=20, blit=False, repeat=False)
        #plt.legend()
        plt.show()
        for obj in Tijelo.objekti:
            print(obj.ime)
    
    def crtanje(frame):
        """for i, obj in enumerate(Tijelo.objekti):
            x_data = [r[0] for r in obj.r[:frame]]
            y_data = [r[1] for r in obj.r[:frame]]
            Tijelo.lines[i].set_data(x_data, y_data)"""
        rep = 100  # broj zadnjih točaka koje crtamo
        for i, obj in enumerate(Tijelo.objekti):
            x_data = [r[0] for r in obj.r[max(0,frame - rep):frame]]
            y_data = [r[1] for r in obj.r[max(0,frame - rep):frame]] #Mora bit max jer prije 100 frameova ne bi bilo slike, od 0 do frame dok je nframes<100
            Tijelo.lines[i].set_data(x_data, y_data)
        return Tijelo.lines
    @staticmethod
    def init():
        Tijelo.lines = []
        for obj in Tijelo.objekti:
            (line,) = Tijelo.ax.plot([], [], label=obj.ime, lw=obj.lw)
            Tijelo.lines.append(line)
        Tijelo.ax.set_xlim(-5e11, 5e11)
        Tijelo.ax.set_ylim(-5e11, 5e11)
        Tijelo.ax.set_xlabel("x/m")
        Tijelo.ax.set_ylabel("y/m")
        Tijelo.ax.legend()
        return Tijelo.lines


Sunce = Tijelo(1.989e30,[0,0], [0,0], "Sunce",5)
Merkur = Tijelo(3.3011e23, [5.791e10,0], [0, 4.787e4], "Merkur")
Mars = Tijelo(6.4171e23, [2.2794e11,0], [0, 2.407e4], "Mars")
Zemlja = Tijelo(5.9742e24,[1.486e11,0],[0, 2.9783e4], "Zemlja")
Venera = Tijelo(4.8675e24, [1.0821e11,0],[0,3.502e4], "Venera")
Komet = Tijelo(1e25,[-4.5*149.6e9,5.791e10],[17e3,2250], "KOMET KOJI CE UNISTIT SVIT") #Valja se igrat sa masom  kometa, da se vidi sudar
Tijelo.gibanje(365.242*24*60*60*2, 3600*12) #2 godine
#Rep u animaciji čak daje predodzbu o brzini; dulji rep - veca brzina