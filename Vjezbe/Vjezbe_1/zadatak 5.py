import numpy as np
import matplotlib.pyplot as plt

def pravac(x1,y1,x2,y2):
    xd=np.linspace(-5,5,10)
    yd= (y2-y1)/(x2-x1)*x + -x1*(y2-y1)/(x2-x1)+y1)
    #print("y = %gx%+g" %((y2-y1)/(x2-x1), -x1*(y2-y1)/(x2-x1)+y1))