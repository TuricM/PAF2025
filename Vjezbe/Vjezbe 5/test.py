import calculus as c
import math as m
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3+x**2+x+1    #KUBNA FUNKCIJA
def g(x):
    return m.sin(x)         #TRIGONOMETRIJSKA FUNKCIJA

cf = c.Calculus(f)
cg = c.Calculus(g)

x = np.linspace(-5,5,50) #Derivacija po tockama za kubnu f-ju
#plt.plot(x, [f(el) for el in x], color="red")
#plt.plot(x, [cf.d_tocka(0.1, f, el) for el in x], color="blue")
dg = cg.d_interval(g,-m.pi,m.pi,0.1) #derivacija po intervalu za trig f-ju
#plt.plot([dg[i][0] for i in range(len(dg))], [g(dg[i][0]) for i in range(len(dg))], color="red")
#plt.plot([dg[i][0] for i in range(len(dg))],[dg[i][1] for i in range(len(dg))], color="blue")

plt.plot(x,[3*t**2+2*t+1 for t in x], color="red", lw=3)
for i in np.arange(0.1,1,10):
    plt.scatter(x, [cf.d_tocka(f, el, i) for el in x], color="blue")
plt.xlabel("x")
plt.ylabel("df/dx")
plt.show()

intp_g = cg.int_pravokutno(g,0,m.pi/2,50)
print("Pravokutna integracija: donja meda: %g | Gornja meda: %g" % (intp_g[0], intp_g[1]))
intt_g = cg.int_trapezno(g,0,m.pi/2,50)
print("Trapezna integracija: %g"%(intt_g))

dom=np.arange(10,200,5) #Baza koraka integracije
plt.scatter(dom, [-(m.cos(m.pi/2)-m.cos(0)) for i in dom], color = "red") #Analiticki
plt.scatter(dom, [cg.int_pravokutno(g,0,m.pi/2,i)[0] for i in dom], color="blue") #Pravokutno(donja meda)
plt.scatter(dom, [cg.int_trapezno(g,0,m.pi/2,i) for i in dom], color="green") #Trapezno
plt.show()