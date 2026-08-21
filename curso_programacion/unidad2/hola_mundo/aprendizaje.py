#programa para cxalcular el IMC
peso = float(input("ingresa tu peso en kg: "))
altura = float(input("ingresa tu altura en metros: "))
imc = peso / (altura **2)
print("tu IMC es:", imc)