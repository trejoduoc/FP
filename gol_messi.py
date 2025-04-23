import os, random, time

# Variables
direccion_balon = 0  # valor ingresado por el usuario range 1 - 5
direccion_arquero = 0  # random entre 1 - 5
intentos = 3
cant_goles = 0
cant_atajadas = 0

# Arte de texto de Messi
arte_messi = '''
⢀⣄⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⣄⡀⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠋⠀⡤⣾⣿⣿⠿⣦⡀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⣸⢼⢿⠵⣈⣧⣙⣗⠀⠀⠀⠀⡼⠁⠊⠀⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠀
⠀⠆⡛⡹⠑⠺⡽⡷⠼⠀⠀⠀⢰⣇⣾⣿⡆⢰⣦⣄⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠈⢯⣳⣴⣄⡸⡿⢴⠀⠀⠀⣾⠀⠀⣮⣀⣈⠀⠁⢸⣻⠀⠀⠀⠀⠀⠀
⠀⠀⢈⠜⣩⠴⣻⡇⣔⡂⠀⠀⠈⣷⣿⠿⠿⠵⣄⣤⡇⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣦⣣⢊⡽⢠⢋⡁⠀⠀⢀⢹⣿⣽⣣⣼⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣤⠘⡷⣳⣿⣷⣠⣴⡆⠈⠻⠿⠿⠟⠁⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠂⣇⣼⣿⣭⣭⣿⡷⡀⠀⠀⠀⠀⠀⣽⡿⣶⢄⡀⠀⠀⠀⠀
⠀⠀⠀⢀⢼⣿⣿⣿⣿⣿⣿⡿⠃⠙⠢⢄⣀⣀⠜⠉⠀⠌⡉⠙⠷⣄⠀⠀
⠀⠀⠀⡀⢠⢻⣿⣟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠑⠀⠈⢷⠀
⠀⠀⢀⢡⣽⣏⢭⡅⡅⣴⢀⣤⠀⠀⢸⡩⡿⢹⠀⠀⣬⡓⡇⢀⠀⠀⠸⠇
⢀⣀⡀⠀⢀⣀⡀⢀⣀⣀⣀⣀⠀⠀⣀⣀⠀⠀⠀⢀⣀⡀⠀⠀⣀⡀⠀⠀
⢸⣿⣿⠀⣾⣿⡇⢸⣿⣟⣛⣛⠀⣾⣟⣛⡿⠆⢰⣿⣛⡿⠷⠀⣿⡇⠀⠀
⢸⣿⢹⣷⡟⣿⡇⢸⣿⡟⠛⠛⠀⣈⡟⠻⣿⡆⣈⣹⠛⢿⣷⠀⣿⡇⠀⠀
⠘⠛⠈⠛⠃⠛⠃⠘⠛⠛⠛⠛⠀⠙⠛⠛⠛⠁⠘⠛⠛⠛⠋⠀⠛⠃⠀⠀
'''

# Código principal
os.system("cls")
print("Bienvenido al juego de Golazo!")
print("El objetivo es hacer un gol al arquero")
print(
    ''' ======= golazo =======
Elige la dirección del tiro (1-5):
1. Angulo superior izquierdo
2. Angulo superior derecho
3. Angulo inferior derecho
4. Angulo inferior izquierdo
5. Centro del arco

''')

while intentos > 0:
    direccion_balon = int(input("Elige la dirección del tiro (1-5): "))
    direccion_arquero = random.randint(1, 5)  # random entre 1 y 5

    if direccion_balon == direccion_arquero:
        cant_atajadas += 1
        print("El arquero atajó el tiro")
    else:
        cant_goles += 1
        print("Golazo!")
        print(f'''
La pelota fue al lado {direccion_balon}
y el arquero fue al lado {direccion_arquero}''')

    intentos -= 1
    print(f"Intentos restantes: {intentos}")
    print(f"Marcador: Goles = {cant_goles}, Atajadas = {cant_atajadas}")
    print("-" * 30)

# Mostrar arte de texto de Messi al final
print("\nJuego terminado!")
print(f"Marcador final: Goles = {cant_goles}, Atajadas = {cant_atajadas}")
if cant_goles > cant_atajadas:
    print("¡Felicidades, ganaste!")
else:
    print("¡El arquero ganó esta vez!")
print(arte_messi)