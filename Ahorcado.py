from random import *

import requests


def obtener_palabra_desde_api():
    url_api = "https://clientes.api.greenborn.com.ar/public-random-word"  # Reemplaza con la URL real de tu API
    try:
        response = requests.get(url_api)
       
        if response.status_code == 200:
            palabra = response.json()[0]  # Ajusta según la estructura de tu respuesta JSON
            return palabra
        else:
            print(f"Error al obtener la palabra. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None



def jugar_de_nuevo():
    respuesta = input("Querés jugar de nuevo? Si/No: ")
    if respuesta == "Si":
        ahorcado()


def pedir_letra():
    return str(input("Elegí una letra: ")).upper()



def ahorcado():
    palabra = list(obtener_palabra_desde_api())
    tablero = []
    vidas = 10
    indice = 0   
    letra_encontrada = False #usar un bool me sirve para recorrer un array entero.

    

    for letra in palabra:
        tablero.append("_")
    print(tablero)

    while vidas >0 and "_" in tablero:
        
        letra_elegida = pedir_letra()

        for letra in palabra:
        
            if letra.upper() == letra_elegida:
                letra_encontrada = True
                tablero[indice] = letra_elegida
                
            indice +=1       
            

        if letra_encontrada :
            print(tablero)
        else:
            vidas -=1
            
        indice = 0
        letra_encontrada = False      
    else:
        if vidas >0:
            print(f"Terminaste el juego!")    

        else:
            print(f"Perdiste!, la palabra era {palabra}")
        jugar_de_nuevo()    





ahorcado()
