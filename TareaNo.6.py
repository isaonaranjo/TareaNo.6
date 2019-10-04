# Maria Isabel Ortiz Naranjo
# Matematica Discreta
# Carnet: 18176
# Fecha: 4/10/2019
# Tarea no. 6 -- Funciones

import numpy as np


# Multiplicacion de las matrices (opcion 1)
def multiplicacionMatrices(fila1, col1, fila2, col2):
    val = 0 # valor inicializado en 0
    matriz1 = np.zeros((fila1, col1))
    matriz2 = np.zeros((fila2, col2))
    # Resultado de la matriz
    final = np.zeros((fila2, col1))
    if col1 == fila2:
        print ("Datos de la primera matriz")
        for i in range(fila1):
            for j in range(col1):
                val = int(input("Introduce 0/1 ("+str(i+1)+","+str(j+1)+") :"))
                matriz1[i][j] = val
        print ("Datos de la segunda matriz")
        for k in range(fila2):
            for l in range(col2):
                val = int(input("Ingrese 0/1 ("+str(k+1)+","+str(l+1)+") :"))
                matriz2[k][l] = val
        final = matriz1 @ matriz2
        print ("\nMatriz final: ", final)
        
# Multiplicacion de matrices (opcion2)
def multMatrices(fila1, col1):
    val = 0 # valor inicializado en 0
    matriz1 = np.zeros((fila1, col1))
    matriz2 = np.zeros((fila1, col1))
    final = np.zeros((fila1, col1))
    if col1 == fila1:
        print ("Datos de la matriz")
        for i in range(fila1):
            for j in range(col1):
                val = int(input("Ingrese 0/1 ("+str(i+1)+","+str(j+1)+") :"))
                matriz1[i][j] = val
                matriz2[i][j] = val
        final = matriz1 @ matriz2
        print ("\nMatriz final: ", final)

# Propiedades de las matrices
def propiedades(fila1, col1):
    val = 0
    matriz1 = np.zeros((fila1, col1))
    antisimetrica = True
    transitiva = True
    reflexiva = True
    simetrica = True
    if col1 == fila1:
        print ("Ingreso de datos: ")
        for i in range(fila1):
            for j in range(col1):
                valor = int(input("Introduce un 0/1 ("+str(i+1)+","+str(j+1)+") :"))
                matriz1[i][j] = val

        # Antisimetrica
        for i in range(fila1):
            for j in range(col1):
                if i != j:
                    if matriz1[i][j] == matriz1[i][j] :
                        antisimetrica = False                       
        # Transitiva
        for i in range(fila1):
            for j in range(col1):
                if matriz1[i][j] == 1:
                    for a in range(fila1):
                        if matriz1[j][a] == 1:
                            if matriz1[i][a] == 0:
                                print(i,"",j,"",a)
                                transitiva = False
        # Reflexividad
        for i in range(fila1):
            if matriz1[i][i] == 0:
                reflexiva = False
                
        # Simetria
        for i in range(fila1):
            for j in range(col1):
                if matriz1[i][j] != matriz1[j][i] :
                    simetrica = False                

        print ("- Antisimetria: "+str(antisimetrica))
        print ("- Transitividad: "+str(transitiva))
        print ("- Reflexividad: "+str(reflexiba))
        print ("- Simetria: "+str(simetrica)+"\n")

# Precedencia 
def precedencia(col1, fila1):
    val = 0
    final = 0
    mayor = 0
    matriz1 = np.zeros((col1, fila1))
    matriz2 = np.zeros((col1, fila1))
    resultado = np.zeros((col1, fila1))
    print ("Datos de la primera matriz")
    for i in range(fila1):
        for j in range(col1):
            val = int(input("Ingrese 0/1 ("+str(i+1)+","+str(j+1)+") :"))
            matriz1[i][j] = valor    
    print ("Datos de la segunda matriz")
    for k in range(fila1):
        for l in range(col1):
            val = int(input("Ingrese 0/1 ("+str(k+1)+","+str(l+1)+") :"))
            matriz2[k][l] = valor
    for i in range(fila1):
        l = False
        for j in range(columnas1):
            if(matriz1[i][j] == matriz2[i][j]):
                mayor == 0
            else:
                l = True
                if matriz1[i][j] > matriz2[i][j]:
                    mayor = 1
                else:
                    mayor = 2
                break
        if l == True:
            break
    #Se verifica que cada elemento de 1 sea mayor que los de 2
    if mayor == 1:
        for i in range(fila1):
            l = False
            for j in range(col1):
                if(matriz1[i][j] < matriz2[i][j]):
                    l = True
                    resultado = 0
                    break
                else:
                    resultado = 2
            if l == True:
                break
                
    #Se verifica que cada elemento de 2 sea mayor que los de 1
    elif mayor == 2:
        for i in range(fila1):
            l = False
            for j in range(col1):
                if(matriz2[i][j] < matriz1[i][j]):
                    l = True
                    resultado = 0
                    break
                else:
                    resultado = 1
            if l == True:
                break
    #Si ninguna es mayor en ningun elemento          
    else:
        resultado = 0

    #Se verifica cual matriz precede a la otra
    if resultado == 1:
        print ("La matriz 1 precede a la matriz 2\n")
    elif resultado == 2:
        print ("La matriz 2 precede a la matriz 1\n")

# Menu de las opciones 
def mainMenu():
    fila1 = 0
    col1 = 0    
    salida = False
    opcion = 0
    fila2 = 0
    col2 = 0

    # Opciones a escoger
    print ("___________                               ________")
    print ("\__    ___/____ _______   ____ _____     /  _____/")
    print ("  |    |  \__  \\_  __ \_/ __ \\__  \   /   __  \ ")
    print ("  |    |   / __ \|  | \/\  ___/ / __ \_ \  |__\  \ ")
    print("   |____|  (____  /__|    \___  >____  /  \_____  /")
    print("               \/            \/     \/         \/ ")
    print ("1. Multiplicacion de matrices asociadas a relaciones de conjuntos distintos (2 matrices)")
    print ("2. Multiplicacion de matrices asociadas a relaciones sobre un conjunto (2 matrices)")
    print ("3. Procedencia de matrices asociadas a relaciones sobre un conjunto (2 matrices)")
    print ("4. Determinar las propiedades")
    print ("5. Salir")
 
    opcion = int(input("Escoge una opcion: "))
 
    if opcion==1:
        print ("\nUsted elegió: Multiplicacion de matrices asociadas a relaciones de conjuntos distintos (2 matrices)")
        fila1 = int(input("Introduce el numero de filas de la primera matriz: "))
        col1 = int(input("Introduce el numero de columnas de la primera matriz: "))
        fila2 = int(input("Introduce el numero de filas de la segunda matriz: "))
        col2 = int(input("Introduce el numero de columnas de la segunda matriz: "))
        multiplicacionMatrices(col1, fila1, col2, fila2)
    elif opcion==2:
        print ("\nMultiplicacion de 2 matrices asociadas a relaciones sobre un conjunto")
        fila1 = int(input("Introduce el numero de filas: "))
        col1 = int(input("Introduce el numero de columnas: "))
        multMatrices(col1, fila1)
    elif opcion==3:
        print("\nProcedencia de matrices asociadas a relaciones sobre un conjunto (2 matrices)")
        fila1 = int(input("Introduce el numero de filas de las dos matrices: "))
        col1 = int(input("Introduce el numero de columnas de ambas matrices: "))
        precedencia(col1, fila1)
    elif opcion==4:
        print("\nDeterminar las propiedades que satisface una matriz")
        fila1 = int(input("Introduce el numero de filas de su matriz: "))
        col1 = int(input("Introduce el numero de columnas de su matriz: "))
        propiedades(fila1, col1)
    elif opcion ==5:
        salir = True
    else:
        print ("Ingresa 1, 2, 3 o 4")

# Funcion del menu

mainMenu()                 
