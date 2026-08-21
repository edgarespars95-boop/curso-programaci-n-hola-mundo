def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma 
numeros = []
for i in range(5):
    valor = int(input(f"Ingrese numero {i+1}: "))
    numeros.append(valor)
total = suma_lista(numeros)
total_sum = sum(numeros) 
print("suma con bucle:", total)
print("suma con sum():", total_sum)