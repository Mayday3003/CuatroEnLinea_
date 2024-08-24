import numpy as np

# DATOS INICIALES
GAME_BOARD1 = (4, 4)  # Tamaño del tablero 4x4
GAME_BOARD2 = (6, 6)  # Tamaño del tablero 6x6

# TODO: Modularizar y optimizar código y agregar comentarios de las funcionalidades de cada parte del código

# MÓDULOS

# MÓDULO 1: BIENVENIDA

def intro():
    """
    Imprime un mensaje de bienvenida con las reglas del juego y pregunta al usuario si está listo para jugar.
    Retorna True si el usuario está listo para jugar, False en caso contrario.
    """
    print(
    """
Bienvenidos a 4 en línea.

Las reglas son sencillas:

-El jugador que complete cuatro fichas en línea (ya sea horizontal, vertical o diagonal) gana la partida.
-Se triplicarán los puntos al jugador que gane dos partidas consecutivas.
-Antes de comenzar, los jugadores deben elegir su nombre y el tamaño del tablero: 4x4 o 6x6.
-Si ninguno de los dos jugadores tiene oportunidad de ganar, aunque el tablero no esté lleno, la partida terminará en empate.
-Después de cada partida, se mostrará el puntaje acumulado de cada jugador.
-Después de cada partida, el sistema preguntará si los jugadores desean seguir jugando.

¿Estás listo para jugar?
a. Sí
b. No""")

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
        print("Vuelve cuando estés preparado para jugar...")
        return False
    
#MÓDULO 2: ELECCIÓN DE NOMBRES
    
def playerName():
    """
    Solicita a los jugadores que ingresen sus nombres y verifica que:
    - Los nombres no estén vacíos.
    - Los nombres sean diferentes entre sí.
    Retorna una tupla con los nombres de los dos jugadores.
    """
    print("Jugador 1, ingresa tu nombre:")
    player1 = input()
    print("Jugador 2, ingresa tu nombre:")
    player2 = input()
    while not (player1.lower().replace(" ", "") and player2.lower().replace(" ", "")):
        if not player1.lower().replace(" ", ""):
            print("El nombre del jugador 1 es inválido, por favor, ingresa otro nombre:")
            print("Jugador 1, ingresa tu nombre:")
            player1 = input()
        else:
            print("El nombre del jugador 2 es inválido, por favor, ingresa otro nombre:")
            print("Jugador 2, ingresa tu nombre:")
            player2 = input()
    while player1.lower().replace(" ", "") == player2.lower().replace(" ", ""):
        print("Los nombres son iguales, por favor, ingresa otros nombres:")
        print("Jugador 1, ingresa tu nombre:")
        player1 = input()
        print("Jugador 2, ingresa tu nombre:")
        player2 = input()
        while not (player1.lower().replace(" ", "") and player2.lower().replace(" ", "")):
            if not player1.lower().replace(" ", ""):
                print("El nombre del jugador 1 es inválido, por favor, ingresa otro nombre:")
                print("Jugador 1, ingresa tu nombre:")
                player1 = input()
            else:
                print("El nombre del jugador 2 es inválido, por favor, ingresa otro nombre:")
                print("Jugador 2, ingresa tu nombre:")
                player2 = input()
    return (player1, player2)
   
#MÓDULO 3: ELECCIÓN DEL TABLERO DE JUEGO

def chooseGameBoard() -> int | str | list[bool]:
    """
    Permite al usuario elegir el tamaño del tablero o salir del juego.
    Retorna una lista con el estado del juego y el tablero seleccionado.
    """
    print("a. Tablero 4x4")
    print("b. Tablero 6x6")
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
        print("Esta opción no está disponible. Elige una opción válida.")
        return [True, False]

# MÓDULO 4: VERIFICAR SI LA CASILLA EXISTE

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

# MÓDULO 5: VERIFICAR SI EL STRING CONTIENE UN NÚMERO

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

# MÓDULO 6: PREDECIR EMPATE

def isThereAWinner(board):
    """
    Verifica si uno de los jugadores tiene posibilidades de ganar en el tablero.
    Retorna True si hay posibilidades de ganar para 'X' o 'O', False en caso contrario.
    """
    # Crea una copia de la lista para trabajar con ella
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)
    
    # Modifica la copia del tablero para probar con el jugador 'X'
    for j in range(checkBoardX.shape[0]):
        for i in range(checkBoardX.shape[1]):
            if checkBoardX[j, i] == 0:
                checkBoardX[j, i] = 'X'
    
    checkBoardX = checkWin(checkBoardX)

    # Modifica la copia del tablero para probar con el jugador 'O'
    for j in range(checkBoardO.shape[0]):
        for i in range(checkBoardO.shape[1]):
            if checkBoardO[j, i] == 0:
                checkBoardO[j, i] = 'O'

    checkBoardO = checkWin(checkBoardO)
    
    # Devuelve True si hay una posible victoria para 'X' o 'O'
    if checkBoardO or checkBoardX:
        return True
    else:
        return False

# MÓDULO 7: IMPRIMIR TABLERO

def printBoard(board):
    """
    Imprime el tablero de juego en formato estético.
    Muestra los números de columna en la parte superior y los números de fila a la izquierda.
    """
    print("   " + "  ".join(f"{i+1:2}" for i in range(board.shape[1])))
    print("  +" + "---+" * board.shape[1])

    for i, row in enumerate(board):
        print(f"{i+1} | " + " | ".join(' ' if x == 0 else x for x in row) + " |")
        print("  +" + "---+" * board.shape[1])

# MÓDULO 8: VERIFICAR GANADOR HORIZONTAL

def checkHorizontal(board):
    """
    Verifica si hay un ganador en el tablero mediante una línea horizontal.
    Retorna True si hay cuatro 'X' o 'O' consecutivos en cualquier fila, False en caso contrario.
    """
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)

    # Verificación horizontal para 'X'    
    for j in range(checkBoardX.shape[0]):
        count = 0
        for i in range(checkBoardX.shape[1]):
            if checkBoardX[j, i] == 'X':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Verificación horizontal para 'O'
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
    
# MÓDULO 9: VERIFICAR GANADOR VERTICAL
def checkVertical(board):
    """
    Verifica si hay un ganador en el tablero mediante una línea vertical.
    Retorna True si hay cuatro 'X' o 'O' consecutivos en cualquier columna, False en caso contrario.
    """
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)    

    # Verificación vertical para 'X'
    for j in range(checkBoardO.shape[0]):
        count = 0
        for i in range(checkBoardO.shape[1]):
            if checkBoardO[i, j] == 'O':
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Verificación vertical para 'O'
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

# MÓDULO 10: VERIFICAR GANADOR DIAGONAL DESCENDENTE
def checkDescendingDiagonal(board):
    """
    Verifica si hay un ganador en el tablero mediante una línea diagonal descendiente.
    Retorna True si hay cuatro 'X' o 'O' consecutivos en cualquier diagonal, False en caso contrario.
    """
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)

    rows, columnas = checkBoardX.shape
    
    # Verificación diagonal principal para 'X'
    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardX[row:row+4, col:col+4]
            
            # Obtener la diagonal descendente principal (de izquierda a derecha)
            diagonal = np.diag(subBoard)
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'X'):
                return True

    # Verificación diagonal principal para 'O'
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

# MÓDULO 11: VERIFICAR GANADOR DIAGONAL ASCENDENTE
def checkAscendinggDiagonal(board):
    """
    Verifica si hay un ganador en el tablero mediante una línea diagonal ascendente.
    Retorna True si hay cuatro 'X' o 'O' consecutivos en cualquier diagonal, False en caso contrario.
    """
    checkBoardX = np.copy(board)
    checkBoardO = np.copy(board)    

    rows, columnas = checkBoardX.shape
    
    # Verificación diagonal inversa para 'X'
    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardX[row:row+4, col:col+4]
            
            # Obtener la diagonal ascendente principal (de izquierda a derecha)
            diagonal = np.diag(np.fliplr(subBoard))
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'X'):
                return True

    # Verificación diagonal inversa para 'O'
    for row in range(rows - 3):
        for col in range(columnas - 3):
            # Extraer la submatriz 4x4 que contiene la diagonal
            subBoard = checkBoardO[row:row+4, col:col+4]
            
            # Obtener la diagonal ascendente principal (de izquierda a derecha)
            diagonal = np.diag(np.fliplr(subBoard))
            
            # Comprobar si todos los elementos de la diagonal son iguales al jugador
            if np.all(diagonal == 'O'):
                return True
    return False

# MÓDULO 12: RECOPILA LAS 4 FUNCIONES ANTERIORES Y VERIFICA SI HAY ALGUN GANADOR EN CUALQUIERA DE LAS MANERAS POSIBLES 
def checkWin(board):
    """
    Verifica si hay un ganador en el tablero.
    Retorna True si hay un ganador, False en caso contrario.
    """
    return checkHorizontal(board) or checkVertical(board) or checkDescendingDiagonal(board) or checkAscendinggDiagonal(board)

# PROGRAMA PRINCIPAL

# Se usa el MÓDULO 1 para dar inicio al juego, empezando por escoger el tablero
if intro():  # Llama a la función intro() para mostrar las reglas y preguntar si el jugador está listo
    play = True  # Inicializa la variable de control del bucle principal del juego
    roundWinX = []  # Lista para almacenar las victorias consecutivas del jugador 1 ('X')
    roundWinO = []  # Lista para almacenar las victorias consecutivas del jugador 2 ('O')
    pointsX = 0  # Inicializa los puntos del jugador 1 ('X')
    pointsO = 0  # Inicializa los puntos del jugador 2 ('O')
    whoWin = None  # Inicializa la variable que almacena el ganador de la ronda
    player1, player2 = playerName()  # Solicita y guarda los nombres de los jugadores

    while play:  # Bucle principal del juego
        print("Elige una opción:")
        gameBoard = chooseGameBoard()  # Permite al jugador elegir el tamaño del tablero o salir
        
        if gameBoard[0] == False:  # Si la opción es salir
            print("Vuelve pronto...")  # Mensaje de despedida
            break  # Sale del bucle principal

        if gameBoard[1] == True:  # Si se eligió un tablero válido
            board = gameBoard[2]  # Selecciona el tablero actual
            printBoard(board)  # Imprime el tablero
            print("Los ceros representan los espacios vacíos.")  # Mensaje informativo
            
            winner = False  # Variable para controlar el estado de la victoria
            round = 0  # Contador de rondas

            while not winner:  # Bucle de juego para cada ronda
                # INTERACCIÓN JUGADOR 1
                print(f"{player1}, elige una casilla:")
                while True:
                    rowX = checkString(input("Elige una fila: "))  # Solicita la fila del jugador 1
                    columnX = checkString(input("Elige una columna: "))  # Solicita la columna del jugador 1

                    # Verifica que las entradas de fila y columna sean válidas
                    while not rowX or not columnX:
                        print("Entrada inválida. Elige una casilla válida:")
                        rowX = checkString(input("Elige una fila: "))
                        columnX = checkString(input("Elige una columna: "))

                    check = checkNumber(rowX[0], columnX[0], board)  # Verifica si la casilla es válida
                    if check[0]:
                        rowX, columnX = check[1:]
                        if board[rowX-1, columnX-1] == 0:  # Verifica si la casilla está vacía
                            board[rowX-1, columnX-1] = 'X'  # Marca la casilla con 'X'
                            break  # Sale del bucle una vez que se haya marcado una casilla válida
                        else:
                            print("Esta casilla está ocupada. Elige otra:")
                    else:
                        print("Casilla no disponible. Elige otra casilla:")

                printBoard(board)  # Imprime el tablero después del movimiento del jugador 1
                if round >= 3 and checkWin(board):  # Verifica si hay un ganador después de 3 rondas
                    whoWin = player1  # El jugador 1 es el ganador
                    pointsX += 1  # Incrementa los puntos del jugador 1
                    break  # Sale del bucle de juego
                if round >= 3:
                    if not isThereAWinner(board):  # Verifica si aún hay posibilidades de ganar
                        print("¡Es un empate!")  # Mensaje de empate
                        break  # Sale del bucle de juego

                # INTERACCIÓN JUGADOR 2
                print(f"{player2}, elige una casilla:")
                while True:
                    rowO = checkString(input("Elige una fila: "))  # Solicita la fila del jugador 2
                    columnO = checkString(input("Elige una columna: "))  # Solicita la columna del jugador 2

                    # Verifica que las entradas de fila y columna sean válidas
                    while not rowO or not columnO:
                        print("Entrada inválida. Elige una casilla válida:")
                        rowO = checkString(input("Elige una fila: "))
                        columnO = checkString(input("Elige una columna: "))

                    check = checkNumber(rowO[0], columnO[0], board)  # Verifica si la casilla es válida
                    if check[0]:
                        rowO, columnO = check[1:]
                        if board[rowO-1, columnO-1] == 0:  # Verifica si la casilla está vacía
                            board[rowO-1, columnO-1] = 'O'  # Marca la casilla con 'O'
                            break  # Sale del bucle una vez que se haya marcado una casilla válida
                        else:
                            print("Esta casilla está ocupada. Elige otra:")
                    else:
                        print("Casilla no disponible. Elige otra casilla:")

                printBoard(board)  # Imprime el tablero después del movimiento del jugador 2

                if round >= 3 and checkWin(board):  # Verifica si hay un ganador después de 3 rondas
                    whoWin = player2  # El jugador 2 es el ganador
                    pointsO += 1  # Incrementa los puntos del jugador 2
                    break  # Sale del bucle de juego
                if round >= 3:
                    if not isThereAWinner(board):  # Verifica si aún hay posibilidades de ganar
                        print("¡Es un empate!")  # Mensaje de empate
                        break  # Sale del bucle de juego
                round += 1  # Incrementa el contador de rondas

            if checkWin(board):  # Verifica si hay un ganador en el tablero
                print(f"{whoWin} ganó.")  # Imprime el nombre del ganador

            # Actualiza las listas de victorias consecutivas y puntos
            if whoWin == player1:
                roundWinX.append(whoWin)  # Agrega el jugador 1 a la lista de victorias consecutivas
                roundWinO = []  # Reinicia la lista de victorias consecutivas del jugador 2
                whoWin = ""  # Reinicia el nombre del ganador
            elif whoWin == player2:
                roundWinO.append(whoWin)  # Agrega el jugador 2 a la lista de victorias consecutivas
                roundWinX = []  # Reinicia la lista de victorias consecutivas del jugador 1
                whoWin = ""  # Reinicia el nombre del ganador
            else:
                roundWinO = []  # Reinicia la lista de victorias consecutivas del jugador 2
                roundWinX = []  # Reinicia la lista de victorias consecutivas del jugador 1
                whoWin = ""  # Reinicia el nombre del ganador
            
            # Multiplica los puntos por 3 si el jugador ha ganado dos rondas consecutivas
            if roundWinX and len(roundWinX) == 2:
                roundWinX = []  # Reinicia la lista de victorias consecutivas del jugador 1
                whoWin = ""  # Reinicia el nombre del ganador
                pointsX *= 3  # Multiplica los puntos del jugador 1 por 3

            elif roundWinO and len(roundWinO) == 2:
                roundWinO = []  # Reinicia la lista de victorias consecutivas del jugador 2
                pointsO *= 3  # Multiplica los puntos del jugador 2 por 3
                whoWin = ""  # Reinicia el nombre del ganador

            # Muestra el puntaje acumulado de cada jugador
            print("")
            print(f"{player1} -> {pointsX}")
            print(f"{player2} -> {pointsO}")

            # Pregunta al usuario si desea seguir jugando
            keepPlaying = True  # Variable de control para continuar jugando
            while keepPlaying:
                print("¿Quieres seguir jugando?")
                print("a. Sí")
                print("b. No")
                answer = input().lower().replace(" ", "")
                if answer == "a":
                    keepPlaying, winner, play = False, True, True  # Continúa jugando
                elif answer == "b":
                    print("Vuelve pronto...")  # Mensaje de despedida
                    keepPlaying, winner, play = False, True, False  # Termina el juego
                else:
                    print("Esta opción no está disponible. Elige otra opción.")  # Mensaje de opción no válida
