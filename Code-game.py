# Frida Arcadia Luna A01711615
""" AHORCADO
Mi proyecto es una adaptación del popular juego de "ahorcado", que en este caso tiene como propósito ayudar a conocer
vocabulario del idioma inglés. Esta versión del juego cuenta con la elección de dos niveles: fácil y difícil.
En el nivel fácil, se presentan palabras que pertenecen a la categoría "colores" (en idioma inglés). En el nivel dificil,
se presentan palabras relacionadas a terminología médica, igualmente en el idioma inglés."""
import random
    
def easy(numused): #Esta función escoge al azar una palabra de la lista
    lista_easy = ['pink', 'brown', 'black', 'green', 'blue', 'orange', 'grey', 'purple', 'yellow', 'white', 'red', 'beige', 'lavander', 'gold', 'silver', 'mint']
    num = random.randint(0,15)
    if num not in numused:
        word = lista_easy[num]
        numused.append(num)
    else:
        num = random.randint(0,15)
        word = lista_easy[num]
        numused.append(num)
    return word, numused
    
def longitud_easy(word): #Esta función define la longitud de la palabra elegida
    x = len(word)
    return x

def lineas_easy(x): #Esta función crea las líneas necesarias para cada letra
    for i in range(x):
        print("_", end = " ")
        
def lista_easy(word): #Esta función crea una lista de la palabra elegida al azar
    lista1 = list(word)
    return lista1

def lista_vacia_easy(lista): #Esta función crea la lista vacía de la palabra elegida al azar
    listav = []
    for i in range(0, len(lista)):
        listav.append('_')
    return listav

def palabra_easy(lista, listav, letra, encuentra): #Esta función acepta la letra sugerida por el usuario y la busca en la palabra. Si la encuntra, la pone en su lugar. Si no, continua colocando un _
    encuentra1 = False
    for i in range(len(lista)):
        if lista[i].lower() == letra.lower():
            listav[i] = letra
            encuentra = encuentra + 1
            encuentra1 = True
    return encuentra, encuentra1
    
######
  
def hard(numusedh): #Esta función escoge al azar una palabra de la lista
    lista_hard = ['headache', 'injection', 'goosebumps', 'abdominoplasty', 'prescription', 'immunity', 'addiction', 'craving', 'organism', 'anticoagulants', 'biochemical']
    num = random.randint(0,10)
    if num not in numusedh:
        word = lista_hard[num]
        numusedh.append(num)
    else:
        num = random.randint(0,10)
        word = lista_hard[num]
        numusedh.append(num)
    return word, numusedh

def longitud_hard(word): #Esta función define la longitud de la palabra elegida
    x = len(word)
    return x

def lineas_hard(x): #Esta función crea las líneas necesarias para cada letra
    for i in range(x):
        print("_", end = " ")
        
def lista_hard(word): #Esta función crea una lista de la palabra elegida al azar
    lista1 = list(word)
    return lista1
        
def lista_vacia_hard(lista): #Esta función crea la lista vacía de la palabra elegida al azar
    listav = []
    for i in range(0, len(lista)):
        listav.append('_')
    return listav

def palabra_hard(listah, listavh, letrah, encuentrah): #Esta función acepta la letra sugerida por el usuario y la busca en la palabra. Si la encuntra, la pone en su lugar. Si no, continua colocando un _
    encuentrah1 = False
    for i in range(len(listah)):
        if listah[i].lower() == letrah.lower():
            listavh[i] = letrah
            encuentrah = encuentrah + 1
            encuentrah1 = True
    return encuentrah, encuentrah1

def imprime_archivo(): #Esta función imprime las instrucciones
    file = open("hangman.txt", 'r')
    contenido = file.read()
    print(contenido)

########
        
def menu(): #Esta función imprime el menú
    print("\n1. Easy. Colors")
    print("2. Hard. Medical vocabulary")
    
def main(): #Ejecuta los pasos en orden
    continua = True
    numused = []
    numusedh = []
    imprime_archivo()
    while continua == True:
        menu()
        opcion = int(input("\nSelect an option: "))
        hola = True #Cierra ciclo que pide que insertes una letra
        cont = 0
        if opcion == 1:
            vidas = 5
            encuentra = 0
            print()
            print("❤❤❤❤❤")
            word, numused = easy(numused)
            x = longitud_easy(word)
            lineas_easy(x)
            lista = lista_easy(word)
            listav = lista_vacia_easy(lista)
            listava = []
            while hola == True:
                if vidas > 0:
                    letra = input("\nInsert a letter: ")
                    res, encuentra1 = palabra_easy(lista, listav, letra, encuentra)
                    print(listav)
                    if letra.lower() not in lista:
                        listava.append(letra)
                        print()
                        print("Letters used", listava)
                    encuentra = res
                    if encuentra1 == False:
                        vidas = vidas - 1
                    print()
                    print("❤" * vidas)
                    if vidas == 0:
                        print("GAME OVER X_X")
                        continua = False
                    elif res == x:
                        print("YOU WON! :D")
                        hola = False
        elif opcion == 2:
            vidash = 7
            encuentrah = 0
            print("❤❤❤❤❤❤❤")
            word, numusedh = hard(numusedh)
            x = longitud_hard(word)
            lineas_hard(x)
            listah = lista_hard(word)
            listavh = lista_vacia_hard(listah)
            listavah = []
            while hola == True:
                if vidash > 0:
                    letrah = str(input("\nInsert a letter: "))
                    res, encuentrah1 = palabra_hard(listah, listavh, letrah, encuentrah)
                    print(listavh)
                    if letrah.lower() not in listah:
                        listavah.append(letrah)
                        print()
                        print("Letters used", listavah)                        
                    encuentrah = res
                    if encuentrah1 == False:
                        vidash = vidash - 1
                    print()
                    print("❤" * vidash)
                    if vidash == 0:
                        print("GAME OVER X_X")
                        continua = False
                    elif res == x:
                        print("YOU WON! :D")
                        hola = False
        else:
            print("\nNon valid option")
            
main()
