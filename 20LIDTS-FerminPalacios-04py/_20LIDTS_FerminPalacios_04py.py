maxf=3
maxc=3

a=[[0.0]*maxc for _ in range(maxf)]

#leer array
for f in range(maxf):
    for c in range(maxc):
        print("ingrese un valor: ")
        a[f][c]=float(input())

print("impresion de valores almacenados")
for f in range(maxf):
    for c in range(maxc):
        print(str(a[f][c]) +" ")
    print()

