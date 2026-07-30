def reemplazar_manual(texto, viejo, nuevo):
    if len(viejo) != 1 or len(nuevo) != 1:
        return texto, 0
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == viejo:
           resultado += nuevo
           contador += 1
        else:
            resultado += letra
    return resultado, contador
texto = input("cadena: ,")
car_viejo = input("caracter areemplazar: ")
car_nuevo = input("caracter nuevo: ")

if len(car_viejo) != 1 or len(car_nuevo) != 1:
    print("Debe ingresaun solo caracter")
else:
    texto_mod, num = reemplazar_manual(texto, car_viejo, car_nuevo)
    texto_mod2 = texto.replace(car_viejo, car_nuevo)
    print("manual:", texto_mod, "|reemplazos:",num)
    print("con replace:", texto_mod2)
    if texto_mod == texto_mod2:
        print("correcro")
        