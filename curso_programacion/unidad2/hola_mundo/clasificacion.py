#clasificasion de calificaciones
nota = float(input("ingrese calificasion: "))
if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"
print("tu calificación es:", letra)