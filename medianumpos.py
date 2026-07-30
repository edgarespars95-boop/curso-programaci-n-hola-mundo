#Media de numeros positivos 
suma = 0
contador = 0
while True:
    num = float(input("numero positivo (negativo sale): "))
    if num < 0:
        break
    if num > 0:
        suma += num
        contador += 1
if contador > 0:
    media = suma / contador
    print("media:", media)
else:
    print("Nose ingresaron positivos")