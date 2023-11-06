from supabase import create_client
import json

supabase = create_client("https://ktehsxolhqumtnvpqoce.supabase.co","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt0ZWhzeG9saHF1bXRudnBxb2NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYzMTc1MjIsImV4cCI6MjAxMTg5MzUyMn0.xB3p8XVTAFHwBH6Q1callbfUEZNHqWkJFnxj5G6fucE")

def CrearDatos():
    while True:
        try:
            deck = input("Introduce el nombre del mazo: ")
            character = input("Selecciona el personaje \n 1 \n 2 \n -> ")
            charInt = int(character)
            #comprobacion de nombre mazo
            if deck != "" and charInt != None or charInt > 0:
                prueba = {"de_name":deck,"de_character_id":charInt}
                supabase.table('decks').insert(prueba).execute()
                Menu()
                break
            else:
                print("No puede ser el nombrte.")
        except:
            print("Ponga solo letras en el nombre del mazo \ En personaje ponga lo que esta indicado")            
    
def MostrarDatos():
    datos = supabase.table('decks').select("*").execute()
    for dato in datos:
        for x in dato:
            deck = json.dumps(x, indent = 2)
            print(deck)
            
    Menu()
    
def ModificarDatos():
    
    bucle = True
    bucle2 = True
    while bucle:
        modify = input("Ponga el nombre del mazo que quiere cambiar: ")
        bbdd = supabase.table('decks').select("de_name").eq("de_name", modify).execute()
        bbddJson = json.loads(bbdd.model_dump_json())
        try:
            if modify == bbddJson["data"][0]["de_name"]:
                
                print(bbddJson["data"][0]["de_name"])
                while bucle2:
                    modifyNew = input("Eleige lo que quieres cambiar: \n 1 - Nombre mazo \n 2 - Id character \n -> ")
                    try:
                        if int(modifyNew) == 1:
                            nameDeck = input("Pon el nuevo nombre al mazo: ")
                            supabase.table('decks').update({"de_name": nameDeck}).eq("de_name",modify).execute()
                            bucle2 = False
                            bucle = False 
                        elif int(modifyNew) == 2:
                            idCharacter = input("Pon el nuevo id del mazo al personaje: ")
                            supabase.table('decks').update({"de_character_id": idCharacter}).eq("de_name",modify).execute()
                            bucle2 = False
                            bucle = False
                    except:
                        print("No es un numero \ Ponga el numero indicado")
        except:           
            print("No esta en la BBDD")
    Menu()
    
def DeleteDatos():
    bucle = True
    while bucle:
        delete = input("Ponga el nombrte del mazo que quiere borrar: ")
        bbdd = supabase.table('decks').select("de_name").eq("de_name", delete).execute()
        bbddJson = json.loads(bbdd.model_dump_json())           
        try:
            if delete == bbddJson["data"][0]["de_name"]:
                supabase.table('decks').delete().eq("de_name",delete).execute()
                bucle = False
        except:           
            print("No esta en la BBDD")    
    Menu()
              
def Menu():    
    while True:
        try:
            menu = input("MENU: \n 1 - Crear datos en mazo \n 2 - Mostrar datos en mazo \n 3 - Modificar datos de mazo \n 4 - Borrar datos de mazo \n -> ")
            menuInt = int(menu)
            if menuInt == 1:
                CrearDatos()
                break
            if menuInt == 2:
                MostrarDatos()
                break
            if menuInt == 3:
                ModificarDatos()
                break
            if menuInt == 4:
                DeleteDatos()
                break
        except:
            print("Ponga lo que le indique el menu")
            
Menu()