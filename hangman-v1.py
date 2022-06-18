#Random:permite obtener distintos numeros o letras de modo aleatorio. 
import random 
#Os:provee funciones para interactuar con el sistema operativo:
import os
#Time: provee funciones relacionadas con el tiempo.
import time



def read_data (filepath="./ani_zoo.txt"): 
    words = [] 
    with open(filepath, 'r', encoding='utf-8') as a:
        for line in a:

            words.append(line.strip().upper())
            #.append: agrega un elemento al final de una lista.
            #.strip: elimina los caracteres vacios
            #.upper: convierte las letras en mayúsculas.
                      
    return words

def read_data2 (filepath="./ani_mascotas.txt"): 
    words2 = []
    with open(filepath, 'r', encoding='utf8') as b: 
        for line2 in b: 
            words2.append(line2.strip().upper())
    
    return(words2)


def run():

    print ("Juego del ahorcado:")
    time.sleep(1)
    print ("El objetivo del juego es adivinar la palabra secreta (sobre animales) letra por letra.")
    print ("Tienes 10 vidas. Pierdes una vida cada que te equivocas.")
    time.sleep(2)

    #seleccionar categorias:

    print ("Categoria A: Animales de Zoo")
    print ("Categoria M: Mascotas")
    select_category = input("¿Cual categoria desea jugar? Seleccione entre A y M: ")


    while True:

        #Una vez el jugador selecciona una categoría válida se ocupa la función choice() para seleccionar una palabra random de esa categoría.

        if select_category.upper() == "A":
            print ("Ha seleccionado para el juego la categoria: Animales de zoo.")
            data = read_data(filepath="./ani_zoo.txt")
            secret_word = random.choice(data)
            break

        elif select_category.upper() == "M":
            print("Ha seleccionado para el juego la categoria: Mascotas.")
            data2 = read_data2(filepath="./ani_mascotas.txt")
            secret_word = random.choice(data2)
            break

        else: 
            print ("Por favor ingrese una letra valida")
            select_category = input("¿Cual categoria desea jugar? Seleccione entre A y M:")
    

    #Definir vidas
    lifes = 10
    #Almacenar palabras adivinadas en una lista:
    list_guessed_words = []

    #Imprimir la palabra pero sin letras
    #len: Devuelve el número de caracteres.
    print("_" *len(secret_word))
    
 
    
    while True:

        while True:
            
            guessed_word = input("Ingresa una letra: ").strip().upper()
            #.strip: elimina los caracteres vacios
            #.upper: convierte las letras en mayúsculas.
            #.isnumeric: Comprueba si todos los caracteres son numericos o no (True or False)
            
            if(len(guessed_word)!=1 and guessed_word.isnumeric()):
                print("Eso no es una letra intenta con una sola letra.")
            else:
                if guessed_word.upper() in list_guessed_words:
                    print("Ya habias intentado con esa letra intenta con otra por favor.")
                else:
                    list_guessed_words.append(guessed_word)
    
                    if guessed_word.upper() in secret_word:
                        print("Felicidades adivinaste una letra.")
                        break
                    else:
                        lifes = lifes-1
                        print("Te haz equivocado y perdido una vida.")
                        print("Te quedan " + str(lifes) + " vidas")
                        break
    
        if lifes==0:
            print("Haz perdido la palabra secreta era: "+ secret_word)
            break               
    

        status_actual = ""
    
        missing_words = 0
        for word in secret_word:
    
    
            if word in list_guessed_words:
                status_actual = status_actual + word
    
            else:
                status_actual = status_actual + "_"
                missing_words = missing_words + 1

        print(status_actual)
 

        if missing_words == 0:
            print("Felicidades haz ganado.")
            print("La palabra secreta es: " + secret_word)
            break
    
        
if __name__ == '__main__':
    run ()