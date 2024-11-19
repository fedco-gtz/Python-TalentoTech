# |---------------------------------------------------------------------|
# | Ejercicio 4 - Mostrar toda la información de un álbum en particular |
# |                                                                     |
# | Listas: Escribe un programa que recorra la lista discografia_lista  |
# | y muestro solo la informacion del album “Thriller”.                 |
# | Se puede mostrar en formato lista.                                  |
# |                                                                     |
# | Diccionarios: Similarmente, recorrer el diccionario                 |
# | discografia_diccionario y mostrar solo la informacion del album     |
# | “Thriller”                                                          |
# |---------------------------------------------------------------------|

discografia_lista = [
    ["Queen",
    "A Night At The Opera",
    "Rock",
    1975,
    12],

    ["Pink Floyd",
    "The Dark Side of the Moon",
    "Progressive Rock",
    1973,
    10],

    ["Led Zeppelin",
        "Led Zeppelin IV",
        "Hard Rock",
        1971,
        8],
    
    ["Madonna",
        "Like A Virgin",
        "Pop",
        1984,
        9],
    
    ["The Beatles",
    "Abbey Road",
    "Rock",
    1969,
    17],
    
    ["Michael Jackson",
    "Thriller",
    "Pop",
    1982,
    9],
    
    ["Eagles",
    "Hotel California",
    "Rock",
    1976,
    9]
]

discografia_diccionario = [
    {
        "Artista": "Queen",
        "Álbum": "A Night At The Opera",
        "Género": "Rock",
        "Año": 1975,
        "Número de canciones": 12,
    },
    {
        "Artista": "Pink Floyd",
        "Álbum": "The Dark Side of the Moon",
        "Género": "Progressive Rock",
        "Año": 1973,
        "Número de canciones": 10,
    },
    {
        "Artista": "Led Zeppelin",
        "Álbum": "Led Zeppelin IV",
        "Género": "Hard Rock",
        "Año": 1971,
        "Número de canciones": 8,
    },
    {
        "Artista": "Madonna",
        "Álbum": "Like A Virgin",
        "Género": "Pop",
        "Año": 1984,
        "Número de canciones": 9,
    },
    {
        "Artista": "The Beatles",
        "Álbum": "Abbey Road",
        "Género": "Rock",
        "Año": 1969,
        "Número de canciones": 17,
    },
    {
        "Artista": "Michael Jackson",
        "Álbum": "Thriller",
        "Género": "Pop",
        "Año": 1982,
        "Número de canciones": 9,
    },
    {
        "Artista": "The Eagles",
        "Álbum": "Hotel California",
        "Género": "Rock",
        "Año": 1976,
        "Número de canciones": 9,
    },
]

# Recorro la lista y muestro información del álbum "Thriller"
for album in discografia_lista:
    if album[1] == "Thriller":
        print("Información del álbum 'Thriller':", album)
        break

# Recorro el diccionario y muestro información del álbum "Thriller"
for album in discografia_diccionario:
    if album["Álbum"] == "Thriller":
        print("Información del álbum 'Thriller':", album)
        break