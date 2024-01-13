from random import *

palabras = ["Palangana", "Raquideo", "Salmonela", "Chinchulin", "Estrepitoso", "Planero"]


def elegir_palabra():
    
    return palabras[randint(0,5)]



def pedir_letra():
    return str(input("Elegí una letra: ")).upper()



def ahorcado():
    palabra = list(elegir_palabra())
    tablero = []
    vidas = 6
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





ahorcado()