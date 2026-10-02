def ConvertirTexteEnMorse(texte):
    # Table Morse
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    }

    # Résultat final
    resultat = ""

    # Parcours texte
    for caractere in texte:
        # Met en majuscule
        caractere = caractere.upper()

        # Vérifie espace
        if caractere == " ":
            resultat = resultat + "/ "

        # Vérifie lettre
        elif caractere in morse:
            resultat = resultat + morse[caractere] + " "

        # Caractère invalide
        else:
            print("Caractère ignoré :", caractere)

    # Retourne résultat
    return resultat


# Titre programme
print("=== Convertisseur de texte en code Morse ===")

# Demande texte
texte = input("Entrez un mot ou une phrase (sans accents, lettres A-Z) : ")

# Conversion Morse
resultat = ConvertirTexteEnMorse(texte)

# Affiche résultat
print("Résultat en Morse :", resultat)
