x=[0,0]
y=[0,0]

for i in range(2):   
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
print("y = %gx%+g" %((y[1]-y[0])/(x[1]-x[0]), -x[0]*(y[1]-y[0])/(x[1]-x[0])+y[0]))
        


    
