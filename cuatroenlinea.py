import numpy as np

# DATOS INICIALES
GAME_BOARD1 = (4, 4)  # Tamaño del tablero 4x4
GAME_BOARD2 = (6, 6)  # Tamaño del tablero 6x6

# MÓDULOS

# MÓDULO 1: ELEGIR TABLERO
def chooseGameBoard() -> int | str:
    """
    Permite al usuario elegir el tamaño del tablero o salir del juego.
    Retorna una tupla con el estado del juego y el tablero seleccionado.
    """
    print("a. Tablero 4x4")
    print("b. Tablero 6X6")
    print("c. Salir")
    answer = input().lower().replace(" ", "")
    
    if answer == "a":
        # Retorna True para continuar, True para jugar y el tablero 4x4 vacío
        return (True, True, np.zeros(GAME_BOARD1, dtype=object))
    elif answer == "b":
        # Retorna True para continuar, True para jugar y el tablero 6x6 vacío
        return (True, True, np.zeros(GAME_BOARD2, dtype=object))
    elif answer == "c":
        # Retorna False para salir del juego
        return (False,)
    else:
        # Mensaje de error si la opción no es válida
        print("Esta opción no está disponible, elige una opción que sí esté disponible")
        return (True, False)

# MÓDULO 2: VERIFICAR SI LA CASILLA EXISTE
def checkNumber(rowX, columnX, gameBoard) -> tuple:
    """
    Verifica si las coordenadas de fila y columna son números válidos y están dentro del rango del tablero.
    Retorna una tupla con un booleano y las coordenadas convertidas a enteros.
    """
    if rowX.isdigit() and columnX.isdigit():
        rowX = int(rowX)
        columnX = int(columnX)
        if 1 <= rowX <= gameBoard.shape[0] and 1 <= columnX <= gameBoard.shape[1]:
            return (True, rowX, columnX)
    return (False,)

# MÓDULO 3: VERIFICAR SI EL STRING CONTIENE UN NÚMERO
def checkString(string):
    """
    Procesa una cadena para extraer todos los números en ella.
    Retorna una lista de números en formato de cadena.
    """
    myList = list(string)
    processed = []
    currentString = ""
    for item in myList:
        if item.isdigit():
            currentString += item
        elif currentString:
            processed.append(currentString)
            currentString = ""
    if currentString:
        processed.append(currentString)
    return processed

# MÓDULO 4: PREDECIR EMPATE
def isThereAWinner(board):
    # Crea una copia de la lista para trabajar con ella
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)
    
    # Modifica la copia de X
    for j in range(checkBoardX.shape[0]):
        for i in range(checkBoardX.shape[1]):
            if checkBoardX[j, i] == 0:
                checkBoardX[j, i] = 'X'
    
    checkBoardX = checkWin(checkBoardX)

    for j in range(checkBoardO.shape[0]):
        for i in range(checkBoardO.shape[1]):
            if checkBoardO[j, i] == 0:
                checkBoardO[j, i] = 'O'

    checkBoardO = checkWin(checkBoardO)
    """
    Revisa si uno de los 2 jugadores tiene posibilidades de ganar o no
    PD: En un futuro, en lugar de los prints, se van a retornar valores booleanos para continuar o no con el juego
    """
    if checkBoardO or checkBoardX:
        print("Sigue Jugando")
    else:
        print("Es un empate")

#MÓDULO 5: Genera un checkBoardX más estetico
def printBoard(board):
    print("   " + "  ".join(f"{i+1:2}" for i in range(board.shape[1])))
    print("  +" + "---+" * board.shape[1])

    for i, row in enumerate(board):
        print(f"{i+1} | " + " | ".join(' ' if x == 0 else x for x in row) + " |")
        print("  +" + "---+" * board.shape[1])

#MÓDULO 6: Comprueba si hay un ganador
def checkHorizontal(board):
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)

    
    for j in range(checkBoardX.shape[0]):
        count = 0
        for i in range(checkBoardX.shape[1]):
            if checkBoardX[j, i] == 'X':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False


    for j in range(checkBoardO.shape[0]):
        count = 0
        for i in range(checkBoardO.shape[1]):
            if checkBoardO[j, i] == 'O':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False
    

def checkVertical(board):
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)    

    for j in range(checkBoardO.shape[0]):
        count = 0
        for i in range(checkBoardO.shape[1]):
            if checkBoardO[i, j] == 'O':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    for j in range(checkBoardX.shape[0]):
        count = 0
        for i in range(checkBoardX.shape[1]):
            if checkBoardX[i, j] == 'X':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

def checkDescendingDiagonal(board):
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)

    rows, columnas = checkBoardX.shape
    
    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardX[row:row+4, col:col+4]
            
            # Obtener la diagonal descendente principal (de izquierda a derecha)
            diagonal = np.diag(subBoard)
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'X'):
                return True


    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardO[row:row+4, col:col+4]
            
            # Obtener la diagonal descendente principal (de izquierda a derecha)
            diagonal = np.diag(subBoard)
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'O'):
                return True
    return False
                
def checkAscendinggDiagonal(board):
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)    
    possible = 0

    rows, columnas = checkBoardX.shape
    
    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardX[row:row+4, col:col+4]
            
            # Obtener la diagonal descendente principal (de izquierda a derecha)
            diagonal = np.diag(np.fliplr(subBoard))
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'X'):
                return True

    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardO[row:row+4, col:col+4]
            
            # Obtener la diagonal descendente principal (de izquierda a derecha)
            diagonal = np.diag(np.fliplr(subBoard))
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'O'):
                return True
    return False
                
def checkWin(board):
    if checkHorizontal(board) or checkVertical(board) or checkDescendingDiagonal(board) or checkAscendinggDiagonal(board):
        return True
    return False
# PROGRAMA PRINCIPAL

# Se usa el MÓDULO 1 para dar inicio al juego, empezando por escoger el checkBoardX
print("Elige una opción")
gameBoard = chooseGameBoard()

while gameBoard[0] != False:
    if gameBoard[1] == True:
        playing = True
        while playing:
            board = gameBoard[2]  # Selecciona el tablero actual
            printBoard(board)
            print("Los ceros representan los espacios disponibles")
            winner = False
            
            round = 0
            while not winner:
                # INTERACCIÓN JUGADOR 1
                print("Jugador 1, elige una casilla")
                while True:
                    rowX = checkString(input("Elige una fila:  "))
                    columnX = checkString(input("Elige una columna:  "))

                    # Verifica que las entradas de fila y columna sean válidas
                    while not rowX or not columnX:
                        print("Entrada inválida. Elige una casilla válida")
                        rowX = checkString(input("Elige una fila:  "))
                        columnX = checkString(input("Elige una columna:  "))

                    check = checkNumber(rowX[0], columnX[0], board)
                    if check[0]:
                        rowX, columnX = check[1:]
                        if board[rowX-1, columnX-1] == 0:
                            board[rowX-1, columnX-1] = 'X'
                            break  # Salir del bucle una vez que se haya marcado una casilla válida
                        else:
                            print("Esta casilla está ocupada, elige otra:")
                    else:
                        print("Casilla no disponible. Elige otra casilla")

                printBoard(board)
                if round >= 3:
                    isThereAWinner(board) #Se comprueba si aun hay posibilidades de ganar despues de cada vuelta.

                # INTERACCIÓN JUGADOR 2
                print("Jugador 2, elige una casilla")
                while True:
                    rowO = checkString(input("Elige una fila:  "))
                    columnO = checkString(input("Elige una columna:  "))

                    # Verifica que las entradas de row y columna sean válidas
                    while not rowO or not columnO:
                        print("Entrada inválida. Elige una casilla válida")
                        rowO = checkString(input("Elige una fila:  "))
                        columnO = checkString(input("Elige una columna:  "))

                    check = checkNumber(rowO[0], columnO[0], board)
                    if check[0]:
                        rowO, columnO = check[1:]
                        if board[rowO-1, columnO-1] == 0:
                            board[rowO-1, columnO-1] = 'O'
                            break  # Salir del bucle una vez que se haya marcado una casilla válida
                        else:
                            print("Esta casilla está ocupada, elige otra:")
                    else:
                        print("Casilla no disponible. Elige otra casilla")

                printBoard(board)
                if round >= 3:
                    isThereAWinner(board) #Se comprueba si aun hay posibilidades de ganar despues de cada vuelta.                
                round+=1

            # Pregunta al usuario si desea seguir jugando
            keepPlaying = True
            while keepPlaying:
                print("¿Quieres seguir jugando?")
                print("a. Sí")
                print("b. No")
                answer = input().lower().replace(" ", "")
                if answer == "a":
                    keepPlaying = True
                elif answer == "b":
                    print("Vuelve pronto...")
                    playing = False
                else:
                    print("Esta opción no está disponible. Elige otra opción")
    else:
        # Si la opción de continuar es falsa, se vuelve a elegir el tablero
        gameBoard = chooseGameBoard()

print("Vuelve pronto...")

