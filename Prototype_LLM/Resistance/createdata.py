import pandas as pd

# Code couleur standard pour chiffres significatifs
colors = {
    "noir": 0,
    "marron": 1,
    "rouge": 2,
    "orange": 3,
    "jaune": 4,
    "vert": 5,
    "bleu": 6,
    "violet": 7,
    "gris": 8,
    "blanc": 9
}

# Multiplicateurs
multipliers = {
    "noir": 1,
    "marron": 10,
    "rouge": 100,
    "orange": 1000,
    "jaune": 10000,
    "vert": 100000,
    "bleu": 1000000,
    "violet": 10000000,
    "or": 0.1,
    "argent": 0.01
}

# Tolérances possibles
tolerances = ["or", "argent"]

# Générer la database
data = []
for b1 in colors:
    for b2 in colors:
        for mult in multipliers:
            for tol in tolerances:
                value = (colors[b1]*10 + colors[b2]) * multipliers[mult]
                data.append([b1, b2, mult, tol, value])

df = pd.DataFrame(data, columns=["Bande1", "Bande2", "Multiplicateur", "Tolérance", "Valeur"])
df.to_csv("resistances_database.csv", index=False)
print("Database générée ✅")
