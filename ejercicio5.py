planta = {
    "Nombre" : "",
    "Lugar" : "",
    "Dias de riego": "",
    "Tamaño" : "",
}

añadirNombre = False
nombre = False

while añadirNombre == False:
    print("¿Cual es el nombre de la planta?")
    nombrePlanta = input()
    nombre = nombrePlanta.isalpha()
    
    if nombre == True :
        planta["Nombre"] = nombrePlanta
        añadirNombre = True
        print("La planta se ha añadido de forma correcta")
    else:
        print("No se ha podido añadir, vuelve a intentarlo")    
    
añadirlugar = False
lugar = False

while añadirlugar == False:
    print("¿Cual es el lugar de la planta?")
    lugarPlanta = input()
    lugar = lugarPlanta.isalpha()
    
    if lugar == True :
        planta["Lugar"] = lugarPlanta
        añadirlugar = True
        print("El lugar se ha añadido de forma correcta")
    else:
        print("No se ha podido añadir, vuelve a intentarlo")    
    
añadirdias = False
dias = False

while añadirdias == False:
    print("¿Cuales son los dias de riego?")
    diasPlanta = input()
    dias = diasPlanta.isdigit()
    
    if dias == True :
        planta["Dias de riego"] = diasPlanta
        añadirdias = True
        print("Los dias de riego se han añadido de forma correcta")
    else:
        print("No se ha podido añadir, vuelve a intentarlo")    
    
añadirtamaño = False
tamaño = False

while añadirtamaño == False:
    print("¿Cual es el tamaño de la planta?")
    tamañoPlanta = input()
    tamaño = tamañoPlanta.isdigit()
    
    if tamaño == True :
        planta["Tamaño"] = tamañoPlanta
        añadirtamaño = True
        print("El tamaño se han añadido de forma correcta")
    else:
        print("No se ha podido añadir, vuelve a intentarlo")    
print(planta)