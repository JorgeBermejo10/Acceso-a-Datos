print("Introduce el valor de la base del triangulo, este valor no puede ser negativo")
base = input()
basenum = int(base)

while basenum <= 0:
    print ("El numero introducido no es valido")
    base = input()
    basenum = int(base)


print("Introduce el valor de la altura del triangulo , este valor no puede ser negativo")
alt = input()
altnum = int(alt)

while altnum <= 0:
    print ("El numero introducido no es valido")
    alt = input()
    altnum = int(alt)
    
area = (basenum * altnum)/2
print("El area del triangulo es", area)


