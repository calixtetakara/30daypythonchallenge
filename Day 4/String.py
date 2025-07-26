# 1. Concaténation
resultat = "trente" + " " + "jours" + " " + "de" + " " + "python"
print("1:", resultat)  # trente jours de python

# 2. Concaténation
resultat = "codage" + " " + "pour" + " " + "tous"
print("\n2:", resultat)  # codage pour tous

# 3. Variable société
societe = "codage pour tous"

# 4. Impression variable
print("\n4:", societe)  # codage pour tous

# 5. Longueur chaîne
print("\n5:", len(societe))  # 16

# 6. Majuscules
print("\n6:", societe.upper())  # CODAGE POUR TOUS

# 7. Minuscules
print("\n7:", societe.lower())  # codage pour tous

# 8. Formatage
chaine = "Coding For All"
print("\n8:")
print("Capitalize:", chaine.capitalize())  # Coding for all
print("Title:", chaine.title())       # Coding For All
print("Swapcase:", chaine.swapcase())    # cODING fOR aLL

# 9. Premier mot
premier_mot = chaine.split()[0]
print("\n9:", premier_mot)  # Coding

# 10. Vérification mot
print("\n10:", "codage" in societe)  # True

# 11. Remplacement
nouvelle_chaine = societe.replace("codage", "Python")
print("\n11:", nouvelle_chaine)  # Python pour tous

# 12. Correction
chaine = "Python pour tout le monde"
chaine_corrigee = chaine.replace("tout le monde", "tous")
print("\n12:", chaine_corrigee)  # Python pour tous

# 13. Split par espace
mots = societe.split()
print("\n13:", mots)  # ['codage', 'pour', 'tous']

# 14. Split par virgule
entreprises = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
liste_entreprises = entreprises.split(", ")
print("\n14:", liste_entreprises)

# 15. Caractère index 0
print("\n15:", chaine[0])  # P

# 16. Dernier index
print("\n16:", len(chaine) - 1)  # 13

# 17. Caractère index 10
print("\n17:", societe[10])  # 'u'

# 18. Acronyme Python
mots = "Python pour tout le monde".split()
acronyme = "".join([mot[0] for mot in mots])
print("\n18:", acronyme)  # Pptm

# 19. Acronyme codage
mots = societe.split()
acronyme = "".join([mot[0] for mot in mots])
print("\n19:", acronyme)  # cpt

# 20. Position 'C'
print("\n20:", chaine.index('C'))  # 0

# 21. Position 'F'
print("\n21:", "Coding For All".index('F'))  # 7

# 22. Dernière 'l'
print("\n22:", "Coding For All".lower().rfind('l'))  # 13

# 23. Première "parce que"
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
print("\n23:", phrase.find("parce que"))  # 42

# 24. Dernière "parce que"
print("\n24:", phrase.rindex("parce que"))  # 53

# 25. Découpage "parce que parce que"
debut = phrase.find("parce que")
fin = phrase.rindex("parce que") + len("parce que")
print("\n25:", phrase[debut:fin])  # "parce que parce que"

# 26. Position première "parce que"
print("\n26:", phrase.index("parce que"))  # 42

# 27. Découpage (identique à 25)
print("\n27:", phrase[debut:fin])  # "parce que parce que"

# 28. Commence par Coding?
print("\n28:", societe.startswith("Coding"))  # False

# 29. Termine par coding?
print("\n29:", societe.endswith("coding"))  # False

# 30. Strip
chaine = "   Codage pour tous   "
print("\n30:", chaine.strip())  # "Codage pour tous"

# 31. Identifier
print("\n31:")
print("30daysofpython:", "30daysofpython".isidentifier())  # False
print("Thirty_days_of_python:", "Thirty_days_of_python".isidentifier())  # True

# 32. Join liste
bibliotheques = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("\n32:", " ".join(bibliotheques))  # "Django Flask Bottle Pyramid Falcon"

# 33. Nouvelle ligne
phrase = "J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape."
print("\n33:")
print(phrase)

# 34. Tabulation
entete = "Name\tAge\tCountry\tCity"
donnees = "Asabeneh\t250\tFinland\tHelsinki"
print("\n34:")
print(entete)
print(donnees)

# 35. Formatage cercle
rayon = 10
aire = 3.14 * rayon ** 2
print("\n35:")
print(f"RADIUS = {rayon} Zone = 3.14 * RADIUS ** 2 La zone d'un cercle avec le rayon {rayon} est de {aire} mètres carrés.")

# 36. Opérations
a, b = 8, 6
print("\n36:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")