# ==============================================
# EXERCICES NIVEAU 1 - MANIPULATION DE SETS DE BASE
# ==============================================

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Trouver la longueur du set it_companies
print("1. Longueur de it_companies:", len(it_companies))  # Résultat: 7

# 2. Ajouter 'Twitter' à it_companies
it_companies.add('Twitter')
print("\n2. Après ajout de Twitter:", it_companies)

# 3. Insérer plusieurs entreprises d'un coup
it_companies.update(['Netflix', 'Tesla', 'Alibaba'])
print("\n3. Après ajout multiple:", it_companies)

# 4. Supprimer une entreprise (IBM)
it_companies.remove('IBM')
print("\n4. Après suppression d'IBM:", it_companies)

# 5. Différence entre remove() et discard()
# remove() lève une exception si l'élément n'existe pas
# discard() ne fait rien si l'élément n'existe pas
try:
    it_companies.remove('Samsung')  # Lèvera KeyError
except KeyError:
    print("\n5. remove() sur élément inexistant lève une exception")

it_companies.discard('Samsung')  # Ne fait rien
print("   discard() sur élément inexistant ne fait rien")

# ==============================================
# EXERCICES NIVEAU 2 - OPÉRATIONS SUR LES ENSEMBLES
# ==============================================

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Union de A et B
print("\n1. Union A ∪ B:", A.union(B))

# 2. Intersection de A et B
print("2. Intersection A ∩ B:", A.intersection(B))

# 3. A est-il un sous-ensemble de B?
print("3. A sous-ensemble de B?", A.issubset(B))  # True

# 4. A et B sont-ils disjoints?
print("4. A et B disjoints?", A.isdisjoint(B))  # False

# 5. Union dans les deux sens
print("5. A union B == B union A?", A.union(B) == B.union(A))  # True

# 6. Différence symétrique
print("6. Différence symétrique A ∆ B:", A.symmetric_difference(B))

# 7. Suppression des sets
del A, B
print("7. Sets A et B supprimés")

# ==============================================
# EXERCICES NIVEAU 3 - APPLICATIONS PRATIQUES
# ==============================================

# 1. Conversion liste -> set
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("\n1. Liste ages:", ages, "longueur:", len(ages))
print("   Set ages:", ages_set, "longueur:", len(ages_set))
print("   La liste est plus longue car contient des doublons")

# 2. Différence entre types de données
print("\n2. Différences entre types:")
print("   - String: séquence immuable de caractères (ex: 'hello')")
print("   - List: séquence mutable et ordonnée (ex: [1, 2, 3])")
print("   - Tuple: séquence immuable et ordonnée (ex: (1, 2, 3))")
print("   - Set: collection mutable, non-ordonnée d'éléments uniques (ex: {1, 2, 3})")

# 3. Comptage de mots uniques
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("\n3. Phrase:", sentence)
print("   Mots uniques:", unique_words)
print("   Nombre de mots uniques:", len(unique_words))