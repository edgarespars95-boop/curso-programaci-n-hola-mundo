#convertidor de monedas
cantidad = float(input("contidad en MXN: "))
print("Monedas  1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion = int(input("eleguir moneda: "))
match opcion:
    case 1:
        resultado = cantidad / 18.14
        moneda = "USA"
    case 2:
        resultado = cantidad / 20.5
        moneda = "EUR"
    case 3:
        resultado = cantidad / 0.55
        moneda = "THB"
    case 4:
        resultado = cantidad / 0.14
        moneda = "JPY"
    case 5:
        resultado = cantidad / 0.014
        moneda = "KRW"
    case 6:
        resultado = cantidad / 13.5
        moneda = "AUD"
    case 7:
        resultado = cantidad / 5.5
        moneda = "PEN"
    case 8:
        resultado = cantidad / 14.5
        moneda = "CAD"
    case 9:
        resultado = cantidad / 0.000004
        moneda = "VES" 
    case 10:
        resultado = cantidad / 0.046
        moneda = "ARS"
    case _:
        resultado = None
        print("opcion no valida")
if resultado is not None:
    print("el equvalente es:" , resultado , moneda)