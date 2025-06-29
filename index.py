# Juego de adivinar el número:

# 1. El juego comienza pidiendo al usuario su nombre.
# 2. Luego muestra un mensaje explicando las reglas: el jugador debe adivinar un número entre 0 y 100.
# 3. El jugador tiene un total de 8 intentos para adivinar el número secreto.
# 4. Por cada intento, el programa validará la entrada del jugador y responderá:
#    - Si el número está fuera del rango (menor que 1 o mayor que 100), mostrará un mensaje de error y pedirá otro número.
#    - Si el número es menor que el número secreto, informará que el número es demasiado bajo.
#    - Si el número es mayor que el número secreto, informará que el número es demasiado alto.
#    - Si el número es correcto, felicitará al jugador e indicará en cuántos intentos lo logró.
# 5. El juego termina si el jugador adivina el número o si se agotan los 8 intentos.

import random

#1. Para pedir el nombre:

name = input("Dame tu nombre: ")
print (f"\n Hola, {name}!")

#2. Explicar las reglas del juego

print ("Voy a pensar en un número entre 1 y 100. Tienes 8 intentos para adivinarlo")

#3. Para generar el número secreo

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 8

#4. Empieza el juego

while intentos < max_intentos:
    try:
        adivinanza = int(input (f"\nIntento {intentos+1}: Adivina el número:"))

        #Validar que está dentro del rango
        if adivinanza < 1 or adivinanza > 100:
            print ("El número debe estar entre 1 y 100. Intentalo de nuevo")
            continue
        intentos +=1

        if adivinanza < numero_secreto:
            print("Demasiado bajo")
        elif adivinanza > numero_secreto:
            print("Demasiado alto")
        else:
            print (f"¡Felicidades, {name}! Adivinaste el número en {intentos} intentos")
            break
    except ValueError:
        print("Por favor, introduce un número válido")

#5. Si no adivina el número

if intentos == max_intentos and adivinanza != numero_secreto:
    print (f"\n Lo siento. {name}. Se te acabaron los intentos. El número era {numero_secreto}")