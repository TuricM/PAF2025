import numpy as np
import math as m

class Calculus:
    def __init__(self, f):
        self.f=f
    def d_tocka(self,f,x, h, metoda=0): #metoda: 0 3point 1 2point
        #h=0.1
        if metoda == 0:
            df = (f(x+h)-f(x-h))/(2*h)
        else:
            df = (f(x+h)-f(x))/h
        return df
    
    def d_interval(self, f, a, b, h, metoda=0): #a donja b gornja
        x = np.linspace(a,b,50)
        der = []
        if metoda == 0:
            for t in x:
                df = (f(t+h)-f(t-h))/(2*h)
                der.append([t,df]) #tocka | njena derivacija
        else:
            for t in x:
                df = (f(t+h)-f(t))/h
                der.append([t,df]) #tocka | njena derivacija
        return der
        
    def int_pravokutno(self,f,a,b,n): # int[a,b]f(x)dx
        dm = 0 #Donja međa
        gm = 0 #Gornja međa
        x=a
        dx = (b-a)/n #Širina pravokutnika
        for i in range(n):
            f_max=f(x)
            f_min=f(x)
            for j in np.arange(x,x+dx,50): #Tražimo lokalni minimum i maksimum u pravokutniku
                if f(j) > f_max :
                    f_max = f(j)
                if f(j) < f_min :
                    f_min = f(j)
            dm+=dx*f_min
            gm+=dx*f_max
            x+=dx
        return [dm,gm]
    def int_trapezno(self,f,a,b,n):
        dx = (b - a) / n  # širina svakog trapeza
        integral = 0.5 * (f(a) + f(b))  # početna vrijednost (krajevi intervala)
    
        for i in range(1, n):
            x = a + i * dx
            integral += f(x)
    
        integral *= dx
        return integral
