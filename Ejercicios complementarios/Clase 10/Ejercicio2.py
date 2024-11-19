# |---------------------------------------------------|
# | Ejercicio 2 - Preguntas sobre la familia de Messi |
# |                                                   |
# | 1. ¿Cuántos hijos tiene Messi?                    |
# |                                                   |
# | 2. ¿Cómo se llaman los hijos de Messi?            |
# |                                                   |
# | 3. ¿Quién es el segundo hijo de Messi?            |
# |                                                   |
# |---------------------------------------------------|

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

# 1. ¿Cuántos hijos tiene Messi?
cantidad_hijos = len(persona["Hijos"])
print("Cantidad de hijos:", cantidad_hijos)

# 2. ¿Cómo se llaman los hijos de Messi?
nombres_hijos = persona["Hijos"]
print("Nombres de los hijos:", ", ".join(nombres_hijos))

# 3. ¿Quién es el segundo hijo de Messi?
segundo_hijo = persona["Hijos"][1]
print("Segundo hijo:", segundo_hijo)