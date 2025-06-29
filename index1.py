# Juego del ahorcado:
# 1. Generar una lista de palabras 
# 2. La aplicacion eligira una palabra alazar 
# 3. Enseñar la cantidad de palabras que tiene la palabra secreta
# 4. Crear una funcion que nos pida una letra. 
# 5. Validar la letra y ensañar todas las que coinciden con la palabra secreta
# 6. Con cada fallo se nos restara una vida
# 7. La cantidad de vidas es de 6
# 6. El juego termina cuando el usuario haya colocado todas las letras que tiene la palabra secreta

import random

# 1. Lista de palabras
palabras = ["python", "manzana", "programa", "ahorcado", "juego", "teclado"]

# 2. Elegir palabra al azar
palabra_secreta = random.choice(palabras)

# 3. Mostrar cantidad de letras
letras_adivinadas = ["_"] * len(palabra_secreta)
vidas = 6

print("🎮 ¡Bienvenido al juego del ahorcado!")
print(f"La palabra secreta tiene {len(palabra_secreta)} letras: {' '.join(letras_adivinadas)}")

# 4. Función para pedir una letra
def pedir_letra():
    while True:
        letra = input("\n📝 Escribe una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("❌ Entrada inválida. Escribe solo una letra.")

# 5-6-7. Lógica del juego
letras_intentadas = []

while True:
    # Mostrar estado actual
    print(f"\nPalabra: {' '.join(letras_adivinadas)}")
    print(f"Letras usadas: {', '.join(letras_intentadas)}")
    print(f"Vidas restantes: {vidas}")

    # Pedir letra
    letra = pedir_letra()

    if letra in letras_intentadas:
        print("⚠️ Ya has intentado esta letra. Intenta con otra.")
        continue
    else:
        letras_intentadas.append(letra)

    if letra in palabra_secreta:
        print("✅ ¡Bien! La letra está en la palabra.")
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                letras_adivinadas[i] = letra
    else:
        vidas -= 1
        print(f"❌ Letra incorrecta. Te quedan {vidas} vidas.")

    # Verificar si se ganó
    if "_" not in letras_adivinadas:
        print(f"\n🎉 ¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
        break

    # Verificar si se perdió
    if vidas == 0:
        print(f"\n💀 Has perdido. La palabra era: {palabra_secreta}")
        break