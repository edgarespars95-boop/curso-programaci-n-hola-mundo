#programa para calcular el salario neto
salario_bruto = float(input("ingresa tu salario bruto: "))
porsentaje = float(input("% impuesto: "))
deducciones = float(input("deducciones:"))
impuestos = salario_bruto * (porsentaje / 100)
salario_neto = salario_bruto - impuestos - deducciones
print("tu salario neto:", salario_neto)