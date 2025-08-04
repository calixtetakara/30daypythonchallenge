# 1. Filtre des nombres négatifs et zéro
nombres = [-4, -3, -2, -1, 0, 2, 4, 6]
filtres = [x for x in nombres if x <= 0]
print("1. Nombres négatifs et zéro:", filtres)  # [-4, -3, -2, -1, 0]

# 2. Aplatir une liste de listes
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplati = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print("\n2. Liste aplatie:", aplati)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Création de tuples avec compréhension de liste
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("\n3. Tuples calculés:", result[:3], "...")  # Affiche les 3 premiers pour l'exemple

# 4. Transformation de liste de pays (version simplifiée)
pays = [[('Finlande', 'Helsinki')], [('Suède', 'Stockholm')], [('Norvège', 'Oslo')]]
output = [[pays, pays[:3], capital] for [[pays, capital]] in pays]
print("\n4. Liste de pays transformée:", output)

# 5. Conversion en liste de dictionnaires
dict_pays = [{'country': p, 'City': c} for [[p, c]] in pays]
print("\n5. Liste de dictionnaires:", dict_pays)

# 6. Concaténation de noms
noms = [[('Asabeneh', 'encoreayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenes = [f"{prenom} {nom}" for [[prenom, nom]] in noms]
print("\n6. Noms concaténés:", concatenes)

# 7. Fonction lambda pour équation linéaire
pente = lambda x1, y1, x2, y2: (y2 - y1)/(x2 - x1)
intercept_y = lambda x, y, m: y - m*x

# Exemple d'utilisation
x1, y1 = 1, 2
x2, y2 = 3, 4
m = pente(x1, y1, x2, y2)
b = intercept_y(x1, y1, m)
print("\n7. Équation linéaire:")
print(f"Pour les points ({x1},{y1}) et ({x2},{y2})")
print(f"L'équation est: y = {m:.1f}x + {b:.1f}")