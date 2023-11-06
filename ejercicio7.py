Asignaturas = ( "iOS", "PSP", "Acceso a datos", "Diseño de interfaces", "Inglés")

def asignaturamodificada() :
    global Asignaturas
    modificada = input("¿Cual asignatura quieres modificar?\n")
    asignueva = input("¿Por cual asignatura quieres cambiarla?\n")
    Imodificada = Asignaturas.index(modificada)
    
    _Asignaturas = list(Asignaturas)
    _Asignaturas[Imodificada] = asignueva
    Asignaturas = tuple(_Asignaturas)
    
print("Asignaturas actuales: \n")
for asig in Asignaturas :
    print(asig + "\n")
    
respuesta = input("¿Quieres modificar alguna asignatura?\n")

if respuesta == "si" :
    asignaturamodificada()
    print("Lista de asignaturas:\n")
    for asig in Asignaturas :
        print(asig + "\n")
else :
    print("La liste no se ha modificado")