def es_palindromo(texto):
    texto = texto.lower()
    limpio =""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1], limpio

entrada = input("ingresa una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)

if resultado:
    print("es una palindramo")
else:
    print("no es un palindromo")
print("lingitud de la cadena limpia:", len(cadena_limpia))
        