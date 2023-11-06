
numero = input("Escribe un número\n")

if numero.isdigit() :
    if int(numero) % 2 == 0 :
        print("El número es par")
    else :
        print("El número es impar")
else :
    print("No has introducido ningun número")
