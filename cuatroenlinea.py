import numpy as np
import random
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

# PROGRAMA PRINCIPAL

# Se usa el MÓDULO 1 para dar inicio al juego, empezando por escoger el tablero
print("Elige una opción")
gameBoard = chooseGameBoard()

while gameBoard[0] != False:
    if gameBoard[1] == True:
        playing = True
        while playing:
            board = gameBoard[2]  # Selecciona el tablero actual
            print(board)
            print("Los ceros representan los espacios disponibles")
            winner = False
            
            while not winner:
                # INTERACCIÓN JUGADOR 1
                print("Jugador 1, elige una casilla")
                rowX = checkString(input("Elige una fila:  "))
                columnX = checkString(input("Elige una columna:  "))

                # Verifica que las entradas de fila y columna sean válidas
                while not rowX or not columnX:
                    print("Entrada inválida. Elige una casilla válida")
                    rowX = checkString(input("Elige una fila:  "))
                    columnX = checkString(input("Elige una columna:  "))

                correctBox = False
                while not correctBox:
                    check = checkNumber(rowX[0], columnX[0], board)
                    if check[0]:
                        rowX, columnX = check[1:]
                        correctBox = True
                    else:
                        print("Casilla no disponible. Elige otra casilla")
                        rowX = checkString(input("Elige una fila:  "))
                        columnX = checkString(input("Elige una columna:  "))

                # Marca la casilla elegida por el Jugador 1
                if board[rowX-1, columnX-1] == 0:
                    board[rowX-1, columnX-1] = 'X'
                else:
                    print("Esta casilla está ocupada, elige otra:")
                    continue
                print(board)

                # INTERACCIÓN JUGADOR 2
                print("Jugador 2, elige una casilla")
                rowO = checkString(input("Elige una fila:  "))
                columnO = checkString(input("Elige una columna:  "))

                # Verifica que las entradas de fila y columna sean válidas
                while not rowO or not columnO:
                    print("Entrada inválida. Elige una casilla válida")
                    rowO = checkString(input("Elige una fila:  "))
                    columnO = checkString(input("Elige una columna:  "))

                correctBox = False
                while not correctBox:
                    check = checkNumber(rowO[0], columnO[0], board)
                    if check[0]:
                        rowO, columnO = check[1:]
                        correctBox = True
                    else:
                        print("Casilla no disponible. Elige otra casilla")
                        rowO = checkString(input("Elige una fila:  "))
                        columnO = checkString(input("Elige una columna:  "))

                # Marca la casilla elegida por el Jugador 2
                if board[rowO-1, columnO-1] == 0:
                    board[rowO-1, columnO-1] = 'O'
                else:
                    print("Esta casilla está ocupada, elige otra:")
                    continue
                print(board)
                
            #PARTE NUEVAAA
            # Verifica si alguien ha ganado 
            winner = False
            for i in range(board.shape[0]):
        
                if all(board[i, :] == 'X'):
                    winner = True
                    break
                elif all(board[:, i] == 'X'):
                    winner = True
                    break
                elif all(np.diag(board) == 'X') or all(np.diag(np.fliplr(board)) == 'X'):
                    winner = True
                    break
                elif all(board[i, :] == 'O'):
                 winner = True
                 break
                elif all(board[:, i] == 'O'):
                 winner
                elif all(np.diag(board) == 'O') or all(np.diag(np.fliplr(board)) == 'O'):
                    winner = True
                    break

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

print("Vuelve pronto...")

print("Vuelve pronto...")

print("Vuelve pronto...")
