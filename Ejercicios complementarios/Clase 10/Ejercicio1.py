# |------------------------------------------------------------|
# | Ejercicio 1 - Preguntas sobre información general de Messi |
# |                                                            |
# | 1. ¿Cuál es el nombre completo de Messi?                   |
# |                                                            |
# | 2. ¿Cuántos años tiene Messi?                              |
# |                                                            |
# | 3. ¿En qué fecha nació Messi?                              |
# |                                                            |
# | 4. ¿Messi está casado?                                     |
# |------------------------------------------------------------|

persona = {
    "Nombre": "Lionel Andrés",
    "Apellido": "Messi",
    "Edad": 36,
    "Nacimiento": "24/06/1987",
    "Casado": True,
    "Hijos": ["Thiago", "Mateo", "Ciro"],
    "Clubes": {
        "FC Barcelona": {
            "Años": [2000, 2021],
            "Posiciones": ["Delantero"],
            "Goles": 672,
        },
        "Paris Saint-Germain": {
            "Años": [2021, 2023],
            "Posiciones": ["Delantero"],
            "Goles": 32,
        },
        "Inter Miami": {"Años": [2023, 2024], "Posiciones": ["Delantero"], "Goles": 18},
    },
}

# 1. ¿Cuál es el nombre completo de Messi?
nombre_completo = f"{persona['Nombre']} {persona['Apellido']}"
print("Nombre completo:", nombre_completo)

# 2. ¿Cuántos años tiene Messi?
edad = persona["Edad"]
print("Edad:", edad)

# 3. ¿En qué fecha nació Messi?
nacimiento = persona["Nacimiento"]
print("Fecha de nacimiento:", nacimiento)

# 4. ¿Messi está casado?
casado = persona["Casado"]
print("¿Está casado?", "Sí" if casado else "No")