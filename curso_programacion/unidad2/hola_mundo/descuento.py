#calcula precio con descuento
precio = float(input("precio original:"))
if precio >= 500:
    descuento = 0.25
elif precio >= 200:
    descuento =  0.20
elif precio >=100:
    descuento = 0.10
else:
    descuento = 0.0
    
precio_final = precio - (precio * descuento)
print("precio final con descuento:", precio_final)