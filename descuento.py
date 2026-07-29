#calcula precio con descuento
precio = float(input("precio original:"))
if precio >= 100:
    descuento = 0
elif precio <= 200:
    descuento =  0.10
elif precio <= 500:
    descuento = .20
else:
    descuento = .25
    
precio_final = precio - (precio * descuento)
print("precio final con descuento:", precio_final)