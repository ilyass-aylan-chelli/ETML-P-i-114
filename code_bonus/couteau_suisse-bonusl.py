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
# 5. STEGANOGRAPHIE (PARTIE 3)
# ============================================================

# Table Morse (lettre -> code)
TABLE_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}

# Table inverse (code -> lettre), construite à partir de la première
TABLE_INVERSE = {}
for lettre_table in TABLE_MORSE:
    TABLE_INVERSE[TABLE_MORSE[lettre_table]] = lettre_table

# Caractères invisibles (largeur nulle)
MARQUEUR_POINT = "\u200B"        # ZERO WIDTH SPACE
MARQUEUR_TIRET = "\u200C"        # ZERO WIDTH NON-JOINER
MARQUEUR_SEP_LETTRE = "\u200D"   # ZERO WIDTH JOINER
MARQUEUR_SEP_MOT = "\u2060"      # WORD JOINER

TOUS_LES_MARQUEURS = MARQUEUR_POINT + MARQUEUR_TIRET + MARQUEUR_SEP_LETTRE + MARQUEUR_SEP_MOT

def dossier_telechargements():
    # Dossier Téléchargements de l'utilisateur (C:\Users\ton_nom\Downloads)
    return os.path.join(os.path.expanduser("~"), "Downloads")


def chemin_stegano(numero):
    # Construit le chemin complet : ...\Downloads\stegano1.txt, stegano2.txt, etc.
    return os.path.join(dossier_telechargements(), "stegano" + str(numero) + ".txt")


def nouveau_fichier():
    # Cherche le premier numéro libre
    numero = 1

    while os.path.exists(chemin_stegano(numero)):
        numero = numero + 1

    return chemin_stegano(numero)


def dernier_fichier():
    # Retourne le dernier fichier stegano existant, ou "" s'il n'y en a aucun
    numero = 1
    dernier = ""

    while os.path.exists(chemin_stegano(numero)):
        dernier = chemin_stegano(numero)
        numero = numero + 1

    return dernier


def texte_en_morse(texte):
    # Convertit un texte (A-Z et espaces) en Morse
    # Les lettres sont séparées par " " et les mots par " / "
    mots_morse = []

    for mot in texte.split():
        lettres_morse = []

        for lettre in mot:
            lettres_morse.append(TABLE_MORSE[lettre])

        mots_morse.append(" ".join(lettres_morse))

    return " / ".join(mots_morse)


def morse_en_texte(code):
    # Convertit du Morse (lettres séparées par " ", mots par " / ") en texte
    resultat = ""
    mots = code.split(" / ")

    for i in range(len(mots)):

        # Espace entre les mots
        if i > 0:
            resultat = resultat + " "

        for lettre_morse in mots[i].split(" "):
            if lettre_morse in TABLE_INVERSE:
                resultat = resultat + TABLE_INVERSE[lettre_morse]
            else:
                # Code inconnu : on le signale par un ?
                resultat = resultat + "?"

    return resultat


def morse_en_marqueurs(code):
    # Transforme le Morse en suite de caractères invisibles
    marqueurs = ""
    mots = code.split(" / ")

    for i in range(len(mots)):

        # Séparateur de mot
        if i > 0:
            marqueurs = marqueurs + MARQUEUR_SEP_MOT

        lettres = mots[i].split(" ")

        for j in range(len(lettres)):

            # Séparateur de lettre
            if j > 0:
                marqueurs = marqueurs + MARQUEUR_SEP_LETTRE

            for symbole in lettres[j]:
                if symbole == ".":
                    marqueurs = marqueurs + MARQUEUR_POINT
                else:
                    marqueurs = marqueurs + MARQUEUR_TIRET

    return marqueurs


def marqueurs_en_morse(marqueurs):
    # Transforme une suite de caractères invisibles en Morse
    code = ""

    for caractere in marqueurs:
        if caractere == MARQUEUR_POINT:
            code = code + "."
        elif caractere == MARQUEUR_TIRET:
            code = code + "-"
        elif caractere == MARQUEUR_SEP_LETTRE:
            code = code + " "
        elif caractere == MARQUEUR_SEP_MOT:
            code = code + " / "

    return code


def encoder(texte_porteur, secret):
    # Cache le secret dans le texte porteur
    # Retourne le texte stéganographié, ou "" si le texte porteur est trop court

    code = texte_en_morse(secret)
    marqueurs = morse_en_marqueurs(code)

    # Il faut au moins 1 caractère du texte porteur par marqueur
    if len(texte_porteur) < len(marqueurs):
        return ""

    resultat = ""

    for i in range(len(texte_porteur)):
        resultat = resultat + texte_porteur[i]

        # On ajoute un marqueur invisible après le caractère, tant qu'il en reste
        if i < len(marqueurs):
            resultat = resultat + marqueurs[i]

    return resultat


def decoder(texte_stegano):
    # Retrouve le secret caché dans le texte
    # Retourne "" si aucun marqueur invisible n'est trouvé

    marqueurs = ""

    # On garde seulement les caractères invisibles, dans l'ordre
    for caractere in texte_stegano:
        if caractere in TOUS_LES_MARQUEURS:
            marqueurs = marqueurs + caractere

    if marqueurs == "":
        return ""

    code = marqueurs_en_morse(marqueurs)

    return morse_en_texte(code)


def secret_valide(secret):
    # Vérifie que le secret contient seulement des lettres A-Z et des espaces
    # et au moins une lettre
    a_une_lettre = False

    for caractere in secret:
        if caractere in TABLE_MORSE:
            a_une_lettre = True
        elif caractere != " ":
            return False

    return a_une_lettre


def menu_steganographie():
    while True:

        print("\n===== STEGANOGRAPHIE =====")
        print("1. Encoder (cacher un message)")
        print("2. Décoder (extraire un message caché)")
        print("3. Retour")

        choix = input("Votre choix : ")

        # Encoder
        if choix == "1":

            texte_porteur = input("Texte porteur (ce que l'on verra) : ")

            if texte_porteur.strip() == "":
                print("Erreur : le texte porteur ne peut pas être vide.")
                continue

            secret = input("Message secret à cacher (A-Z et espace) : ").upper()

            if not secret_valide(secret):
                print("Erreur : le message doit contenir uniquement des lettres A-Z et des espaces.")
                continue

            resultat = encoder(texte_porteur, secret)

            if resultat == "":
                print("Erreur : le texte porteur est trop court pour cacher ce message.")
                print("Il faut au moins", len(morse_en_marqueurs(texte_en_morse(secret))), "caractères.")
            else:
                chemin = nouveau_fichier()

                fichier = open(chemin, "w", encoding="utf-8")
                fichier.write(resultat)
                fichier.close()

                print("Le texte avec stéganographie a été sauvegardé dans le fichier", chemin)
                print("Aperçu :", resultat)

        # Décoder
        elif choix == "2":

            nom = input("Nom du fichier à lire (Entrée pour le dernier fichier créé) : ")

            if nom == "":
                nom = dernier_fichier()

            if not os.path.exists(nom):
                print("Erreur : le fichier", nom, "n'existe pas.")
                continue

            fichier = open(nom, "r", encoding="utf-8")
            texte_stegano = fichier.read()
            fichier.close()

            secret = decoder(texte_stegano)

            if secret == "":
                print("Aucun message caché trouvé dans ce texte.")
            else:
                print("Message secret :", secret)

        # Retour
        elif choix == "3":
            break

        else:
            print("Choix invalide.")


# ============================================================
# 6. CODE BONUS : CHIFFREMENT ET DECHIFFREMENT (CESAR ET VIGENERE)
# ============================================================

# Les 26 lettres de l'alphabet, en majuscules et en minuscules
ALPHABET_MAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_MIN = "abcdefghijklmnopqrstuvwxyz"


def cesar(texte, decalage):
    # Décale chaque lettre du texte de "decalage" positions dans l'alphabet
    # Exemple avec un décalage de 3 : A -> D, B -> E, ..., Z -> C
    resultat = ""

    # On regarde chaque caractère du texte
    for caractere in texte:

        # Si c'est une lettre majuscule
        if caractere in ALPHABET_MAJ:
            position = ALPHABET_MAJ.find(caractere)

            # Le % 26 permet de revenir au début de l'alphabet après le Z
            # (en Python, ça marche aussi avec un décalage négatif)
            nouvelle_position = (position + decalage) % 26

            resultat = resultat + ALPHABET_MAJ[nouvelle_position]

        # Si c'est une lettre minuscule
        elif caractere in ALPHABET_MIN:
            position = ALPHABET_MIN.find(caractere)

            nouvelle_position = (position + decalage) % 26

            resultat = resultat + ALPHABET_MIN[nouvelle_position]

        # Sinon (espace, chiffre, accent, ponctuation...) on ne change rien
        else:
            resultat = resultat + caractere

    return resultat


def chiffrer(texte, cle):
    # Chiffrer = décaler vers la droite
    return cesar(texte, cle)


def dechiffrer(texte, cle):
    # Déchiffrer = décaler dans l'autre sens (avec la même clé)
    return cesar(texte, -cle)


def demander_cle():
    # Demande la clé (le décalage) jusqu'à ce que l'utilisateur entre un nombre valide
    while True:

        cle = input("Entrez la clé (un nombre entre 1 et 25) : ")

        # On vérifie que ce sont bien des chiffres
        if not cle.isdigit():
            print("Erreur : la clé doit être un nombre entier.")

        # On vérifie que le nombre est entre 1 et 25
        elif int(cle) < 1 or int(cle) > 25:
            print("Erreur : la clé doit être entre 1 et 25.")

        else:
            return int(cle)


def menu_cesar():
    while True:

        print("\n===== CHIFFRE DE CESAR =====")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Tester toutes les clés (si on ne connaît pas la clé)")
        print("4. Retour")

        choix = input("Votre choix : ")

        # Chiffrer
        if choix == "1":

            texte = input("Message à chiffrer : ")

            if texte.strip() == "":
                print("Erreur : le message ne peut pas être vide.")
                continue

            cle = demander_cle()

            resultat = chiffrer(texte, cle)

            print("Message chiffré :", resultat)

        # Déchiffrer
        elif choix == "2":

            texte = input("Message à déchiffrer : ")

            if texte.strip() == "":
                print("Erreur : le message ne peut pas être vide.")
                continue

            cle = demander_cle()

            resultat = dechiffrer(texte, cle)

            print("Message déchiffré :", resultat)

        # Tester toutes les clés (force brute)
        elif choix == "3":

            texte = input("Message à déchiffrer : ")

            if texte.strip() == "":
                print("Erreur : le message ne peut pas être vide.")
                continue

            # On essaie les 25 clés possibles et on les affiche toutes
            for cle in range(1, 26):
                print("Clé", cle, ":", dechiffrer(texte, cle))

        # Retour au menu principal
        elif choix == "4":
            break

        else:
            print("Choix invalide.")


# ------------------------------------------------------------
# Chiffre de Vigenère
# C'est comme César, mais le décalage change à chaque lettre.
# La clé est un MOT (exemple : "LEMON") et chaque lettre de la clé
# donne un décalage : A = 0, B = 1, C = 2, ..., Z = 25
# ------------------------------------------------------------

def vigenere(texte, cle, sens):
    # sens = 1 pour chiffrer, sens = -1 pour déchiffrer
    resultat = ""

    # Position de la lettre de la clé qu'on utilise en ce moment
    position_cle = 0

    # On met la clé en majuscules pour pouvoir chercher dans ALPHABET_MAJ
    cle = cle.upper()

    for caractere in texte:

        # On ne chiffre que les lettres
        if caractere in ALPHABET_MAJ or caractere in ALPHABET_MIN:

            # Lettre de la clé à utiliser (le % revient au début de la clé quand elle est finie)
            lettre_cle = cle[position_cle % len(cle)]

            # Décalage donné par cette lettre (A = 0, B = 1, ...)
            decalage = ALPHABET_MAJ.find(lettre_cle) * sens

            # On réutilise la fonction cesar() pour décaler cette seule lettre
            resultat = resultat + cesar(caractere, decalage)

            # On passe à la lettre suivante de la clé
            position_cle = position_cle + 1

        # Sinon (espace, chiffre, ponctuation...) on ne change rien
        # et on n'avance PAS dans la clé
        else:
            resultat = resultat + caractere

    return resultat


def cle_vigenere_valide(cle):
    # Vérifie que la clé contient seulement des lettres A-Z et au moins une lettre
    if cle == "":
        return False

    for caractere in cle.upper():
        if caractere not in ALPHABET_MAJ:
            return False

    return True


def menu_vigenere():
    while True:

        print("\n===== CHIFFRE DE VIGENERE =====")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Retour")

        choix = input("Votre choix : ")

        # Chiffrer
        if choix == "1":

            texte = input("Message à chiffrer : ")

            if texte.strip() == "":
                print("Erreur : le message ne peut pas être vide.")
                continue

            cle = input("Clé (un mot, lettres A-Z seulement) : ")

            if not cle_vigenere_valide(cle):
                print("Erreur : la clé doit contenir uniquement des lettres A-Z.")
                continue

            print("Message chiffré :", vigenere(texte, cle, 1))

        # Déchiffrer
        elif choix == "2":

            texte = input("Message à déchiffrer : ")

            if texte.strip() == "":
                print("Erreur : le message ne peut pas être vide.")
                continue

            cle = input("Clé (le même mot que pour chiffrer) : ")

            if not cle_vigenere_valide(cle):
                print("Erreur : la clé doit contenir uniquement des lettres A-Z.")
                continue

            print("Message déchiffré :", vigenere(texte, cle, -1))

        # Retour
        elif choix == "3":
            break

        else:
            print("Choix invalide.")


def menu_bonus():
    while True:

        print("\n=====  BONUS : CHIFFREMENT / DECHIFFREMENT =====")
        print("1. Chiffre de César  (clé = un nombre)")
        print("2. Chiffre de Vigenère  (clé = un mot)")
        print("3. Retour")

        choix = input("Votre choix : ")

        if choix == "1":
            menu_cesar()

        elif choix == "2":
            menu_vigenere()

        # Retour au menu principal
        elif choix == "3":
            break

        else:
            print("Choix invalide.")


# ============================================================
# 7. MENU PRINCIPAL
# ============================================================

def main():
    while True:

        print("\n================================")
        print("       COUTEAU SUISSE")
        print("================================")
        print("1. Convertisseur Morse")
        print("2. Convertisseur de bases  (Décimal <> Binaire <> Octal) ")
        print("3. Stéganographie")
        print("4. Code Bonus  Chiffrement César / Vigenère")
        print("5. Quitter")

        choix = input("Votre choix : ")

        # Ouvre le convertisseur Morse
        if choix == "1":
            morse()

        # Ouvre le convertisseur de bases
        elif choix == "2":
            menu_conversion()

        # Ouvre la stéganographie
        elif choix == "3":
            menu_steganographie()

        # Ouvre le code bonus (chiffrement / déchiffrement)
        elif choix == "4":
            menu_bonus()

        # Quitter le programme
        elif choix == "5":

            input("\nalors appuyer sur Entrer ")

            break

        else:
            print("Choix invalide.")

        input("\nAppuyez sur Entrée pour continuer")


# ============================================================
# Lancement du programme
# ============================================================

main()