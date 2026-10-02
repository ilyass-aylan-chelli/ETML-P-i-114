import os

# ============================================================
# 1. CONVERTISSEUR TEXTE -> MORSE
# ============================================================

def morse():
    # Tableau qui contient les lettres et leur code Morse
    code_morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--.."
    }

    texte = input("Entrez un mot ou une phrase : ")

    resultat = ""

    # On regarde chaque caractère du texte
    for lettre in texte.upper():

        # Si c'est un espace
        if lettre == " ":
            resultat = resultat + "/ "

        # Si la lettre existe dans le tableau
        elif lettre in code_morse:
            resultat = resultat + code_morse[lettre] + " "

        # Si le caractère n'est pas reconnu
        else:
            print("Caractère ignoré :", lettre)

    print("Résultat :", resultat)


# ============================================================
# 2. CONVERTISSEUR DE BASES
# ============================================================

def decimal_binaire(nombre):
    # Convertit en chaîne, garde uniquement les chiffres, puis transforme en entier
    nombre_nettoye = "".join(caractere for caractere in str(nombre) if caractere.isdigit())

    # Si la chaîne est vide (il n'y avait que des lettres), on retourne une chaîne vide ou un message
    if not nombre_nettoye:
        return ""

    nombre = int(nombre_nettoye)

    # Cas spécial si le nombre est 0
    if nombre == 0:
        return "0"

    resultat = ""

    # On divise le nombre par 2 jusqu'à arriver à 0
    while nombre > 0:
        reste = nombre % 2
        resultat = str(reste) + resultat
        nombre = nombre // 2

    return resultat

def binaire_decimal(nombre):
    resultat = 0
    puissance = 0

    # On commence par le dernier chiffre
    for i in range(len(nombre) - 1, -1, -1):
        chiffre = int(nombre[i])

        # Calcul de la valeur décimale
        resultat = resultat + chiffre * (2 ** puissance)

        puissance = puissance + 1

    return resultat


def decimal_octal(nombre):
    # Cas spécial si le nombre est 0
    if nombre == 0:
        return "0"

    resultat = ""

    # On divise le nombre par 8
    while nombre > 0:
        reste = nombre % 8
        resultat = str(reste) + resultat
        nombre = nombre // 8

    return resultat


def octal_decimal(nombre):
    resultat = 0
    puissance = 0

    # On commence par la droite
    for i in range(len(nombre) - 1, -1, -1):
        chiffre = int(nombre[i])

        # Calcul de la valeur décimale
        resultat = resultat + chiffre * (8 ** puissance)

        puissance = puissance + 1

    return resultat


# ============================================================
# 3. VERIFICATION DES NOMBRES
# ============================================================

def est_binaire(nombre):
    # Vérifie que le nombre contient seulement 0 et 1
    for chiffre in nombre:
        if chiffre != "0" and chiffre != "1":
            return False

    return True


def est_octal(nombre):
    # Vérifie que le nombre contient seulement des chiffres de 0 à 7
    for chiffre in nombre:
        if chiffre not in "01234567":
            return False

    return True


# ============================================================
# 4. MENU DES CONVERSIONS
# ============================================================

def menu_conversion():
    while True:

        print("\n===== CONVERTISSEUR DE BASES =====")
        print("1. Décimal -> Binaire")
        print("2. Binaire -> Décimal")
        print("3. Décimal -> Octal")
        print("4. Octal -> Décimal")
        print("5. Binaire -> Octal")
        print("6. Octal -> Binaire")
        print("7. Retour")

        choix = input("Votre choix : ")

        if choix == "1":
            # On garde le texte tel quel (str) pour que la fonction puisse filtrer les lettres
            nombre = input("Entrez un nombre décimal : ")

            resultat = decimal_binaire(nombre)

            # Si l'utilisateur n'a entré que des lettres, on affiche un message d'erreur
            if resultat == "":
                print("Erreur : Vous devez entrer au moins un chiffre.")
            else:
                print("Résultat :", resultat)

        # Binaire -> Décimal
        elif choix == "2":

            nombre = input("Entrez un nombre binaire : ")

            if est_binaire(nombre):
                resultat = binaire_decimal(nombre)
                print("Résultat :", resultat)
            else:
                print("Erreur : ce n'est pas un nombre binaire.")

        # Décimal -> Octal
        elif choix == "3":

            nombre = int(input("Entrez un nombre décimal : "))

            resultat = decimal_octal(nombre)

            print("Résultat :", resultat)

        # Octal -> Décimal
        elif choix == "4":

            nombre = input("Entrez un nombre octal : ")

            if est_octal(nombre):
                resultat = octal_decimal(nombre)
                print("Résultat :", resultat)
            else:
                print("Erreur : ce n'est pas un nombre octal.")

        # Binaire -> Octal
        elif choix == "5":

            nombre = input("Entrez un nombre binaire : ")

            if est_binaire(nombre):

                # On passe d'abord par le décimal
                decimal = binaire_decimal(nombre)

                # Puis du décimal vers l'octal
                resultat = decimal_octal(decimal)

                print("Résultat :", resultat)

            else:
                print("Erreur : ce n'est pas un nombre binaire.")

        # Octal -> Binaire
        elif choix == "6":

            nombre = input("Entrez un nombre octal : ")

            if est_octal(nombre):

                # On passe d'abord par le décimal
                decimal = octal_decimal(nombre)

                # Puis du décimal vers le binaire
                resultat = decimal_binaire(decimal)

                print("Résultat :", resultat)

            else:
                print("Erreur : ce n'est pas un nombre octal.")

        # Retour au menu principal
        elif choix == "7":
            break

        else:
            print("Choix invalide.")

        break


# ============================================================
# 5. MENU PRINCIPAL
# ============================================================

def main():
    while True:

        print("\n================================")
        print("       COUTEAU SUISSE")
        print("================================")
        print("1. Convertisseur Morse")
        print("2. Convertisseur de bases  (Décimal <> Binaire <> Octal) ")
        print("3. Quitter")

        choix = input("Votre choix : ")

        # Ouvre le convertisseur Morse
        if choix == "1":
            morse()

        # Ouvre le convertisseur de bases
        elif choix == "2":
            menu_conversion()

        # Quitter le programme
        elif choix == "3":

            input("\nalors appuyer sur Entrer ")


            break



        else:
            print("Choix invalide.")

        input("\nAppuyez sur Entrée pour continuer")


# ============================================================
# Lancement du programme
# ============================================================

main()
