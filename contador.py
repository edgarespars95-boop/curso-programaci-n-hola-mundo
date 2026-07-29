#contar letras a
palabra = input("ingresa palabla: "). lower()
contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1 
print("la letra 'a' aparece" , contador, "veces")