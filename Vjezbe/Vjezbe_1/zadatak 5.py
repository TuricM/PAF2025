import numpy as np
import matplotlib.pyplot as plt

def pravac(x1,y1,x2,y2):
    xd=np.linspace(-5,5,10)
    yd= (y2-y1)/(x2-x1)*xd + -x1*(y2-y1)/(x2-x1)+y1
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.grid()
    plt.plot(xd,yd)    
    while True:    
        odabir= input("Način prikazivanja(P prozor, D datoteka): ")
        if odabir == "P" or odabir == "p":           
            plt.show()
            break
        elif odabir == "D" or odabir == "d":
            ime = input("Unesi ime datoteke: ")
            plt.savefig(ime+".pdf", format="pdf")
            break
        else:
            print("Krivi unos")
        
    #print("y = %gx%+g" %((y2-y1)/(x2-x1), -x1*(y2-y1)/(x2-x1)+y1))
x=[0,0]
y=[0,0]

for i in range(2):   #Unos kopiran iz zadatka 3
    while True:
        flag1 = 1
        xk = input("Unesi x%d:" % (i+1))
        for el in xk:
            if el not in "0123456789":
                print("Pogrešan unos!")
                flag1=0
                break
        if flag1:
            x[i]=int(xk)
            break
    while True:
        flag1 = 1
        yk = input("Unesi y%d:" % (i+1))
        for el in yk:
            if el not in "0123456789":
                print("Pogrešan unos!")
                flag1=0
                break
        if flag1:
            y[i]=int(yk)
            break
pravac(x[0],y[0],x[1],y[1])
