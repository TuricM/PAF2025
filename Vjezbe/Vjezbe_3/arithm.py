import math as m
import numpy as np

def sredina(podatci):
    return sum(podatci)/len(podatci)
def devijacija(podatci):
    s=sredina(podatci)
    return m.sqrt((sum([(el-s)**2 for el in podatci]))/(len(podatci)))
x=[1,2,3,4,5,6,7,8,9,10]
print("sredina: %g, devijacija: %g" %(sredina(x),devijacija(x)))

print("sredina: %g, devijacija: %g"%(np.mean(x),np.std(x))) #Gotovi moduli