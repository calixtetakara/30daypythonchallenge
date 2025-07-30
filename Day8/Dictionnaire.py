# 1. Créez un dictionnaire vide appelé chien
chien = {}

# 2. Ajouter le nom, la couleur, la race, les jambes, l'âge au dictionnaire pour chiens
chien["nom"] = "Rex"
chien["couleur"] = "marron"
chien["race"] = "Labrador"
chien["jambes"] = 4
chien["âge"] = 5

# 3. Créez un dictionnaire étudiant et ajoutez les clés indiquées
étudiant = {
    "first_name": "Calixte",
    "last_name": "Doe",
    "sexe": "Masculin",
    "âge": 21,
    "état_matrimonial": "Célibataire",
    "compétences": ["React", "TypeScript", "Tailwind", "MUI"],
    "pays": "Togo",
    "ville": "Pya",
    "adresse": "123 Rue de l'Avenir"
}

# 4. Obtenez la longueur du dictionnaire étudiant
longueur = len(étudiant)
print("Longueur du dictionnaire étudiant :", longueur)

# 5. Obtenez les valeurs du dictionnaire comme une liste
valeurs = list(étudiant.values())
print("Valeurs du dictionnaire étudiant :", valeurs)

# 6. Changez le dictionnaire en une liste de tuples avec items()
liste_de_tuples = list(étudiant.items())
print("Dictionnaire en liste de tuples :", liste_de_tuples)

# 7. Supprimer un élément du dictionnaire étudiant (par exemple "ville")
étudiant.pop("ville")
print("Dictionnaire après suppression de 'ville' :", étudiant)

# 8. Supprimer le dictionnaire chien
del chien
# print(chien)  # Ceci renverrait une erreur si décommenté, car 'chien' n'existe plus
