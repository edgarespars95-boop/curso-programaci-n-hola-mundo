#vocales / No vocales
while True:
    letra = input("ingrese letra (espacio termina): ")
    if letra == " ":
        break
    letra = letra.lower()
    if letra in "aeiou":
       print("vocal")
    else:
        print("consonante")
print("programa finalizado") 
                       
                        
                        