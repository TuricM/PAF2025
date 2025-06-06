import numpy as np
import math as mt

class Tijelo:
    objekti=[] #Lista koja sadržava sva tijela
    def __init__(self,m,r_0,v_0):
        self.m=m
        self.r=[r_0]
        self.v=[v_0]
        self.a=[0,0]
        Tijelo.objekti.append(self) #Dodamo tijelo u listu
    
    def akceleracija(self, G=6.67408e-11):
        # m*a=G mM/r**2
        # a_x = a*cosfi = a* x/d
        # a_y = a* y/d
        for obj in Tijelo.objekti:
            d = [obj.r[1][0]-self.r[-1][0], obj.r[1][1]-self.r[-1][1]] # vektor udaljenosti od tijela do nekog objekta
            d_iznos= mt.sqrt(d[0]**2+d[1]**2)
            self.a=[self.a[0]+G*obj.m/(d_iznos**2)*(d[0],d_iznos), self.a[1]+G*obj.m/(d_iznos**2)*(d[1],d_iznos)] #pridonos akceleracije jednog objekta na tijelo
        return 0
    
    def korak(self):
        self.akceleracija()
        self.v.append([self.v[-1][0]])