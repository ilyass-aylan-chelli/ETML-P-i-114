# ETML-P-i-114
Couteau Suisse en Python (application console) : convertisseur de texte en code Morse, convertisseur de bases (décimal / binaire / octal) écrit à la main, et stéganographie par caractères Unicode invisibles. Projet du module 114 – Codification / Chiffrement (ETML).


Application console en Python regroupant plusieurs utilitaires de codification.

## Fonctionnalités
- **Morse** : conversion d'un texte (A-Z, espaces) en code Morse
- **Conversion de bases** : décimal ↔ binaire, binaire ↔ octal, algorithmes écrits
  à la main (sans `int(x, 2)`, `bin()` ni `oct()`), avec validation des saisies
- **Stéganographie** : cache un message Morse dans un texte porteur à l'aide de
  caractères Unicode de largeur nulle (U+200B, U+200C, U+200D, U+2060), puis le
  retrouve au décodage

## Lancer le projet
python main.py

## Contexte
Projet réalisé dans le cadre du module 114 à l'ETML.
