#calculadora basica
while True:
    print("1.suma 2.resta 3.multiplicacion 4.division 5.salir")
    op = int(input("opcion: "))
    if op == 5:
        break
    a = float(input("primer numero: "))
    b = float(input("segundo numero: "))
    match op:
        case 1: print(a + b)
        case 2: print(a - b)
        case 3: print(a * b)
        case 4:
            if b != 0:
                print(a / b)
            else:
                print("error: division por cero")
    resp =input("¿desea continuar? (s/n): ").lower()
    if resp == 'n':
         break