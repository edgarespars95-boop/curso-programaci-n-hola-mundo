#calcula de nota final
parciales = float(input("nota parciales (0-100): "))
proyecto = float(input("nota proyecto (0-100): "))
examen_final = float(input("nota examen final (0-100): "))

if (parciales < 0 or parciales > 100) or (proyecto < 0 or proyecto > 100) or (examen_final < 0 or examen_final > 100):
    print("error: las notas deben estar entre 0 y 100")
else:
    calificasion_final = (parciales * 0.4) + (proyecto * 0.3) + (examen_final * 0.3)
    print("calificacion_final:", calificasion_final)