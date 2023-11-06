import ejercicio1
import ejercicio2
import ejercicio3

abrir = False
while abrir == False:
    print("Que ejercicio desea abrir")
    carpeta: input()
    
    try:
        open(carpeta)
        abrir = True
    
    except:
        print("No existe")