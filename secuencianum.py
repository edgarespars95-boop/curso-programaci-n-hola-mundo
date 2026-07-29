#secuencia aritmetica
inicio = int(input("primer numero"))
diferencia = int(input("diferencia: "))
limite = int(input("limite maximo:"))
num = inicio
while True:
    print(num, end=" ")
    num += diferencia 
    if num > limite:
        break
print("\nsecuencia aritmetica desde", inicio, "hasta", limite)