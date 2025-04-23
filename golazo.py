import os, random, time

# Variables
direccion_balon =0 #valor ingresado por el usuario range 1 - 5
direccion_arquero = 0 #random entre 1 - 5
intentos = 3
cant_goles = 0
cant_atajadas = 0

#codigo principal
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

direccion_balon = int(input("Elige la dirección del tiro (1-5): "))
direccion_arquero = random.randint(1,5) #random entre 1 y 5

while intentos > 0:
    if direccion_balon == direccion_arquero:
        cant_atajadas +=1
        print("Penal Atajado!")
    else:
        direccion_balon != direccion_arquero
        cant_goles +=1
        print("Golazo!")
        
    intentos -= 1    
    print(f'''
            
intentos restantes: {intentos}
goles: {cant_goles}
atajadas: {cant_atajadas}''')
    print ("-"*30)
    
print(f"""Termino el juego!
Esta fue la cantidad de goles: {cant_goles}
Esta fue la cantidad de atajadas: {cant_atajadas}
""")
if cant_goles > cant_atajadas:
    print("GANASTE!")
else:
    print("PERDISTE!")
    