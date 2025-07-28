# ==================== NIVEAU 1 ====================

# 1. Créer un tuple vide
tuple_vide = ()
print("Tuple vide:", tuple_vide)

# 2. Créer des tuples pour frères et sœurs (imaginaires)
freres = ("Jean", "Pierre")
soeurs = ("Marie", "Sophie")
print("\nFrères:", freres)
print("Sœurs:", soeurs)

# 3. Joindre les tuples
freres_et_soeurs = freres + soeurs
print("\nFrères et sœurs réunis:", freres_et_soeurs)

# 4. Compter le nombre de frères et sœurs
nombre = len(freres_et_soeurs)
print("\nNombre total de frères et sœurs:", nombre)

# 5. Ajouter les parents et créer family_members
parents = ("Paul", "Alice")
family_members = freres_et_soeurs + parents
print("\nMembres de la famille:", family_members)

# ==================== NIVEAU 2 ====================

# 1. Déballer le tuple family_members
*freres_soeurs, pere, mere = family_members
print("\nDéballage du tuple:")
print("Frères et sœurs:", freres_soeurs)
print("Père:", pere)
print("Mère:", mere)

# 2. Créer des tuples alimentaires et les combiner
fruits = ("pomme", "banane", "orange")
legumes = ("carotte", "brocoli", "épinard")
produits_animaux = ("lait", "fromage", "œufs")
food_stuff_tp = fruits + legumes + produits_animaux
print("\nTuple food_stuff_tp:", food_stuff_tp)

# 3. Convertir en liste
food_stuff_lt = list(food_stuff_tp)
print("\nListe food_stuff_lt:", food_stuff_lt)

# 4. Trouver l'élément du milieu
milieu = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 1:
    element_milieu = food_stuff_lt[milieu]
else:
    element_milieu = food_stuff_lt[milieu-1:milieu+1]
print("\nÉlément(s) du milieu:", element_milieu)

# 5. Extraire les 3 premiers et 3 derniers éléments
premiers_3 = food_stuff_lt[:3]
derniers_3 = food_stuff_lt[-3:]
print("\n3 premiers éléments:", premiers_3)
print("3 derniers éléments:", derniers_3)

# 6. Supprimer le tuple food_stuff_tp
del food_stuff_tp
print("\nTuple food_stuff_tp supprimé")

# 7. Vérifications sur les pays nordiques
pays_nordiques = ("Norvège", "Suède", "Finlande", "Danemark", "Islande")
print("\nVérifications:")
print("L'Estonie est un pays nordique?", "Estonie" in pays_nordiques)  # False
print("L'Islande est un pays nordique?", "Islande" in pays_nordiques)  # True