#programa para simular el juego de piedra,papel o tijera.
import random

print("------------------------------------------")
print("---------LANZAMIENTO DE UN DADO----------")
print("------------------------------------------")

# input 

# processing

maquina = random.randint(1,3)

# usuario = random.randint(1,3)

jugador= int(input("escoje que sacaras:"))

if (maquina==1): #piedra
    if (jugador==1):
        rta="empate"
    elif (jugador==2):
        rta= "ganaste"
    else: