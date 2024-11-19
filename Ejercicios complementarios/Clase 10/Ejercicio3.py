# |---------------------------------------------------------------------|
# | Ejercicio 3 - Preguntas sobre su carrera futbolística               |
# |                                                                     |
# | 1. ¿Cuántos goles marcó Messi durante su tiempo en el FC Barcelona? |
# |                                                                     |
# | 2. ¿En qué años jugó Messi en el Paris Saint-Germain?               |
# |                                                                     |
# | 3. ¿Cuántos goles lleva Messi en el Inter Miami?                    |
# |                                                                     |
# | 4. ¿Cuántos goles ha marcado Messi en total durante su carrera?     |
# |                                                                     |
# | 5. ¿Cuál es el club donde Messi marcó más goles?                    |
# |---------------------------------------------------------------------|

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

# 1. ¿Cuántos goles marcó Messi durante su tiempo en el FC Barcelona?
goles_barcelona = persona["Clubes"]["FC Barcelona"]["Goles"]
print("Goles en FC Barcelona:", goles_barcelona)

# 2. ¿En qué años jugó Messi en el Paris Saint-Germain?
años_psg = persona["Clubes"]["Paris Saint-Germain"]["Años"]
print("Años en Paris Saint-Germain:", f"{años_psg[0]} - {años_psg[1]}")

# 3. ¿Cuántos goles lleva Messi en el Inter Miami?
goles_inter_miami = persona["Clubes"]["Inter Miami"]["Goles"]
print("Goles en Inter Miami:", goles_inter_miami)

# 4. ¿Cuántos goles ha marcado Messi en total durante su carrera?
goles_totales = sum(club["Goles"] for club in persona["Clubes"].values())
print("Goles totales en su carrera:", goles_totales)

# 5. ¿Cuál es el club donde Messi marcó más goles?
club_mas_goles = max(persona["Clubes"], key=lambda club: persona["Clubes"][club]["Goles"])
print("Club donde marcó más goles:", club_mas_goles)