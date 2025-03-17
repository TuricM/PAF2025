def preciznost(N):
    x=5
    for i in range(N):
        x=x+1/3.0
    for i in range(N):
        x=x-1/3.0
    print(x)

preciznost(200)
preciznost(2000)
preciznost(20000)
#Razlomak 1/3 ne može se zapisati kao konačan binaran broj, pa je i rezultat precizan samo do razine preciznosti binarnog zapisa razlomka 1/3