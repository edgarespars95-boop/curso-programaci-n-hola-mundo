#brinda informacion
consulta = input("ingresa nombre de artista, pelicula o serie:").lower()
match consulta:
    case "inception":
        info = "pelicula de ciencia ficcion dirigida por christopher nolan."
    case "heroes del silencio":
       info = "banda de rock española formada en zaragoza en 1984."
    case "the witcher":
       info = "serie de fantasmas basada en el libro del mismo nombre."
    case "the last of us":
       info = "serie de drama y suspenso basada en el videojuego del mismo nombre."
    case "un show mas":
       info = "serie de comedia animada creada por j.g quintel."
    case _:
        info = "no se encontro informacion."
print("informacion:", info)