import numpy as np

# DATOS INICIALES
GAME_BOARD1 = (4, 4)  # Tamaño del tablero 4x4
GAME_BOARD2 = (6, 6)  # Tamaño del tablero 6x6

#TODO:Modularizar y optimizar codigo y agragar comentarios de las funcionalidades de cada parte del codigo

# MÓDULOS

# MÓDULO 1: ELEGIR TABLERO
def intro():
    print(
    """
Bienvenidos a 4 en linea.

Las reglas son sencillas :

-El jugador que complete cuatro fichas en línea (ya sea horizontal, vertical o diagonal) gana la partida.
-Se triplicarán los puntos al jugador que gane dos partidas consecutivas.
-Antes de comenzar, los jugadores deben elegir el tamaño del tablero: 4x4 o 6x6.
-Si ninguno de los dos jugadores tiene oportunidad de ganar, aunque el tablero no este lleno, la partida terminará en empate.
-Después de cada partida, se mostrará el puntaje acumulado de cada jugador.
-Después de cada partida, el sistema preguntará si los jugadores desean seguir jugando.

¿Estas listo para jugar?
a.Si
b.No""")

    while True:
        answer = input().strip().lower()
        if answer in ["a", "b"]:
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida:")
            print("¿Estás listo para jugar?")
            print("a. Sí")
            print("b. No")
    if answer == "a":
        return True
    else:
        print("Vuelve cuando estes preparado para jugar...")
        return False
    
def playerName ():
    print("Jugador 1, ingresa tu nombre")
    player1 = input()
    print("Jugador 2, ingresa tu nombre")
    player2 = input()
    while not (player1.lower().replace(" ", "") and player2.lower().replace(" ", "")):
        if not player1.lower().replace(" ", ""):
            print("El nombre del jugador 1 es invalido, por favor, ingresa otro nombre")
            print("Jugador 1, ingresa tu nombre")
            player1 = input()
        else:
            print("El nombre del jugador 2 es invalido, por favor, ingresa otro nombre")
            print("Jugador 2, ingresa tu nombre")
            player2 = input()
    while player1.lower().replace(" ", "") == player2.lower().replace(" ", ""):
        print("Los nombres son iguales, por favor, ingresen otros nombres")
        print("Jugador 1, ingresa tu nombre")
        player1 = input()
        print("Jugador 2, ingresa tu nombre")
        player2 = input()
        while not (player1.lower().replace(" ", "") and player2.lower().replace(" ", "")):
            if not player1.lower().replace(" ", ""):
                print("El nombre del jugador 1 es invalido, por favor, ingresa otro nombre")
                print("Jugador 1, ingresa tu nombre")
                player1 = input()
            else:
                print("El nombre del jugador 2 es invalido, por favor, ingresa otro nombre")
                print("Jugador 2, ingresa tu nombre")
                player2 = input()
    return (player1, player2)
   

def chooseGameBoard() -> int | str | list[bool]:
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
        return [True, True, np.zeros(GAME_BOARD1, dtype=object)]
    elif answer == "b":
        # Retorna True para continuar, True para jugar y el tablero 6x6 vacío
        return [True, True, np.zeros(GAME_BOARD2, dtype=object)]
    elif answer == "c":
        # Retorna False para salir del juego
        return [False]
    else:
        # Mensaje de error si la opción no es válida
        print("Esta opción no está disponible, elige una opción que sí esté disponible")
        return [True, False]

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
        return True
    else:
        return False

#MÓDULO 5: Genera un tablero más estetico
def printBoard(board):
    print("   " + "  ".join(f"{i+1:2}" for i in range(board.shape[1])))
    print("  +" + "---+" * board.shape[1])

    for i, row in enumerate(board):
        print(f"{i+1} | " + " | ".join(' ' if x == 0 else x for x in row) + " |")
        print("  +" + "---+" * board.shape[1])

#MÓDULO 6: Comprueba si hay un ganador horizontalmente
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
    
#MÓDULO 7: Comprueba si hay un ganador verticalmente
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

#MÓDULO 8: Comprueba si hay un ganador en la diagonal descendente
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

#MÓDULO 9: Comprueba si hay un ganador en la diagonal ascendente
def checkAscendinggDiagonal(board):
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)    

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

#MÓDULO 10: Recopila las 4 funciones anteriores y comprueba si hay  un ganador de cualquier manera posible  
def checkWin(board):
    if checkHorizontal(board) or checkVertical(board) or checkDescendingDiagonal(board) or checkAscendinggDiagonal(board):
        return True
    return False

# PROGRAMA PRINCIPAL

# Se usa el MÓDULO 1 para dar inicio al juego, empezando por escoger el tablero


if intro():
    play = True
    roundWinX = []
    roundWinO = []
    pointsX = 0
    pointsO = 0
    whoWin = None
    player1, player2 = playerName()
    while play:
        print("Elige una opción")
        gameBoard = chooseGameBoard()
        if gameBoard[0] == False:
            print("Vuelve pronto...")
            break
        if gameBoard[1] == True:
            board = gameBoard[2]  # Selecciona el tablero actual
            printBoard(board)
            print("Los ceros representan los espacios disponibles")
            
            winner = False
            round = 0

            while not winner:
                # INTERACCIÓN JUGADOR 1
                print(f"{player1}, elige una casilla")
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
                if round >= 3 and checkWin(board):
                    whoWin = player1
                    pointsX += 1
                    break       
                if round >= 3: 
                    if not isThereAWinner(board): #Se comprueba si aun hay posibilidades de ganar despues de cada vuelta.
                        print("¡Es un empate!")
                        break 
                # INTERACCIÓN JUGADOR 2
                print(f"{player2}, elige una casilla")
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

                if round >= 3 and checkWin(board):
                    whoWin = player2
                    pointsO += 1
                    break               
                if round >= 3: 
                    if not isThereAWinner(board): #Se comprueba si aun hay posibilidades de ganar despues de cada vuelta.
                        print("¡Es un empate!")
                        break 
                round+=1
            if checkWin(board):
                print(f"{whoWin} gano")
            if whoWin == player1:
                roundWinX.append(whoWin)
                roundWinO = []
                whoWin = ""
            elif whoWin == player2:
                roundWinO.append(whoWin)
                roundWinX = []
                whoWin = ""
            else:
                roundWinO = []
                roundWinX = []
                whoWin = ""
            
            if roundWinX and len(roundWinX) == 2:
                roundWinX = []
                whoWin = ""
                pointsX *= 3

            elif roundWinO and len(roundWinO) == 2:
                roundWinO = []
                pointsO *= 3
                whoWin = ""

            print("")
            print(f"{player1} -> {pointsX}")
            print(f"{player2} -> {pointsO}")

            # Pregunta al usuario si desea seguir jugando
            keepPlaying = True
            while keepPlaying:
                print("¿Quieres seguir jugando?")
                print("a. Sí")
                print("b. No")
                answer = input().lower().replace(" ", "")
                if answer == "a":
                    keepPlaying, winner, play = False, True, True
                elif answer == "b":
                    print("Vuelve pronto...")
                    keepPlaying, winner, play = False, True, False
                else:
                    print("Esta opción no está disponible. Elige otra opción")  