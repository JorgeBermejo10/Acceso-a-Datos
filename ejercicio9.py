instrumentos = {"Flauta", "Guitarra", "Piano"}

def añadir() :
    intrunuevo = input("¿Qué instrumento quieres añadir a la lista? ")
    global instrumentos
    instrumentos.add(intrunuevo)

def cambiarinstrumento() :
    instrumentoMovido = input("¿Qué instrumento quieres que no aparezca en la lista? ")
    global instrumentos
    instrumentos.discard(instrumentoMovido)
    
def lista() :
    global instrumentos
    for instru in instrumentos :
        print(instru)

lista()

while True :
    respuesta = input("¿Quieres añadir o suprimir un elemento?")
    
    if respuesta == "suprimir" :
        cambiarinstrumento()
        lista()
    elif respuesta == "añadir" :
        añadir()
        lista()
    else :
        break
