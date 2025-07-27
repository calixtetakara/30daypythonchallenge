# 1. Déclarer une liste vide
liste_vide = []

# 2. Déclarer une liste avec plus de 5 articles
liste_articles = ["pomme", "banane", "orange", "kiwi", "fraise", "ananas"]

# 3. Trouver la longueur de la liste
longueur = len(liste_articles)
print(f"Longueur de la liste : {longueur}")

# 4. Obtenir le premier, moyen et dernier élément
premier = liste_articles[0]
milieu = liste_articles[len(liste_articles)//2]
dernier = liste_articles[-1]
print(f"Premier: {premier}, Milieu: {milieu}, Dernier: {dernier}")

# 5. Liste mixed_data_types
mixed_data_types = ["Jean", 30, 1.75, "célibataire", "123 Rue Paris"]

# 6. Liste IT_COMPANIES
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimer la liste
print("\nListe IT_COMPANIES:")
print(IT_COMPANIES)

# 8. Nombre d'entreprises
print(f"\nNombre d'entreprises: {len(IT_COMPANIES)}")

# 9. Première, moyenne et dernière société
print(f"Première: {IT_COMPANIES[0]}, Milieu: {IT_COMPANIES[len(IT_COMPANIES)//2]}, Dernière: {IT_COMPANIES[-1]}")

# 10. Modifier et imprimer
IT_COMPANIES[0] = "Meta"
print("\nListe après modification:")
print(IT_COMPANIES)

# 11. Ajouter une société
IT_COMPANIES.append("Twitter")
print("\nAprès ajout de Twitter:")
print(IT_COMPANIES)

# 12. Insérer au milieu
IT_COMPANIES.insert(len(IT_COMPANIES)//2, "Samsung")
print("\nAprès insertion de Samsung:")
print(IT_COMPANIES)

# 13. Changer un nom (sauf IBM)
IT_COMPANIES[2] = "Up It"
print("\nAprès modification:")
print(IT_COMPANIES)

# 15. Vérifier l'existence d'une entreprise
print("\nGoogle est dans la liste?", "Google" in IT_COMPANIES)

# 16. Trier la liste
IT_COMPANIES.sort()
print("\nListe triée:")
print(IT_COMPANIES)

# 17. Inverser la liste
IT_COMPANIES.reverse()
print("\nListe inversée:")
print(IT_COMPANIES)

# 18. Supprimer les 3 premières
del IT_COMPANIES[:3]
print("\nAprès suppression des 3 premières:")
print(IT_COMPANIES)

# 19. Supprimer les 3 dernières
del IT_COMPANIES[-3:]
print("\nAprès suppression des 3 dernières:")
print(IT_COMPANIES)

# 20. Trancher la société du milieu
milieu = IT_COMPANIES[len(IT_COMPANIES)//2]
print(f"\nSociété du milieu: {milieu}")

# 21. Supprimer la dernière société
IT_COMPANIES.pop()
print("\nAprès suppression de la dernière société:")
print(IT_COMPANIES)

# 26. Joindre des listes
front_end = ['html', 'css', 'js', 'react', 'redux'] 
back_end = ['node', 'express', 'mongodb']
full_stack = front_end + back_end
print("\nFull stack:")
print(full_stack)

# 27. Insérer Python et SQL
full_stack = full_stack.copy()
full_stack.insert(full_stack.index("redux")+1, "Python")
full_stack.insert(full_stack.index("Python")+1, "SQL")
print("\nFull stack avec Python et SQL:")
print(full_stack)

# Exercices niveau 2
# 1. Manipulation des âges
print("\n\nEXERCICES NIVEAU 2")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
ages.extend([min_age, max_age])
median = (ages[len(ages)//2] + ages[~(len(ages)//2)]) / 2
moyenne = sum(ages)/len(ages)
plage = max_age - min_age

print("\nÂges:")
print(f"Liste triée: {ages}")
print(f"Min: {min_age}, Max: {max_age}")
print(f"Médiane: {median}")
print(f"Moyenne: {moyenne}")
print(f"Plage: {plage}")

# 2. Manipulation des pays
pays = ["Chine", "Russie", "USA", "Finlande", "Suède", "Norvège", "Danemark"]
pays_scandinaves = pays[3:]
trois_premiers = pays[:3]

print("\nPays:")
print(f"Tous les pays: {pays}")
print(f"Pays scandinaves: {pays_scandinaves}")
print(f"Trois premiers pays: {trois_premiers}")