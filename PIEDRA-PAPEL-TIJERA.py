#programa para simular el juego de piedra,papel o tijera.

import random

# input 

print("----------------------------------------------")
print("---------JUEGO PIEDRA PEPEL O TIJERA----------")
print("----------------------------------------------")

# processing


jugador = int(input("Escoje lo que sacaras, ¡PERO RAPIDO!: "))

maquina = random.randint(1,3)

piedra=1
papel=2
tijera=3

if (maquina==1):#piedra
    if (jugador==1):#piedra
        rta="vaya vaya fue un empate"
    elif (jugador==2):#papel
        rta= "ganaste  wow"
    elif (jugador==3):#tijera
        rta= "---perdiste  jajaja"


if (maquina==2):#papel
        if (jugador==1):#piedra
            rta="---perdiste  jajaja"
        elif (jugador==2):#papel
            rta= "vaya vaya fue un empate"
        elif (jugador==3):#tijera
            rta= "ganaste  wow"


if (maquina==3):#tijera
        if(jugador==1):#piedra
            rta="ganaste  wow"
        elif(jugador==2):#papel
            rta="---perdiste  jajaja"
        elif(jugador==3):#tijera
            rta="vaya vaya fue un empate"


    
if (jugador>3):
    rta = "¡¡¡USTED DIGITÓ UN NÚMERO NO VALIDO!!!"

if(jugador<3):
    rta=print("la maquina saco: " +str(maquina))
    rta=print("usted saco: " +str(jugador))

# output
print(rta)



