#convertidor de temperatura
celsius = float(input("temperatura en °c: "))
print("1. fahrenheit\n2. kelvin")
opcion = int(input("elige una opcion: "))
match opcion:
    case 1:
        resultado = celsius * 9/5 + 32
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("opcion invalida")
if resultado is not None:
    print("convertido:", resultado, unidad)