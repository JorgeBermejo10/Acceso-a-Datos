numeroslista = []
adelante = input()
adel= int(adelante)
while adel == 1 or adel ==2:
    
    print("¿Quieres añadir un numero a tu lista?, pulse 1 para añadir o 2 para finalizar")
    adelante = input()
    adel= int(adelante)

    while adel ==1:
        print("Añade un número a tu lista")
        numeroañadido = int(input())
        
        try:
            numeroañadidoInt = int(numeroañadido)
            numeroslista.append(numeroañadido)
            print("¿Quieres añadir un numero a tu lista?, pulse 1 para añadir o 2 para finalizar")
            adelante = input()
            adel= int(adelante)
        except:
            print("EL valor introducido no es valido")

    if adel == 2 :
        numeroslista.sort()
        print(numeroslista)