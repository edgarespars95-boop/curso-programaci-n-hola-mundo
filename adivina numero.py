#adivinar numero
import random
secreto = random.randint(1, 100)
while True:
    intento = int(input("adivina (1 - 100): "))
    if intento < secreto:
        print("demasiado bajo")
    elif intento > secreto: 
        print("demasiado alto")
    else:
        print("¡correcto! era", secreto)
        break
print("juego terminao. El numero era", secreto)