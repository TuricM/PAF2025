print(str(5-4.935))
#Očekujem 0.065, a dobijem 0.06500000000000039. Razlog je taj što se 4.935 ne može zapisati kao konačan binarni broj, pa je zapis (U ovom slucaju 64-bitovni) precizan samo do određene razine.
print(str(0.1+0.2+0.3))
#Objašnjenje je isto kao za prethodni slučaj. Pribrojnici se ne mogu zapisati kao konačni binarni brojevi pa je njihov zbroj precizan samo do određene razine.
