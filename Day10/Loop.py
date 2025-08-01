# Niveau 1

# 1. Itération de 0 à 10
print("1. Itération de 0 à 10:")
print("Boucle for:")
for i in range(11):
    print(i, end=' ')
print("\nBoucle while:")
i = 0
while i <= 10:
    print(i, end=' ')
    i += 1
print("\n")

# 2. Itération de 10 à 0
print("2. Itération de 10 à 0:")
print("Boucle for:")
for i in range(10, -1, -1):
    print(i, end=' ')
print("\nBoucle while:")
i = 10
while i >= 0:
    print(i, end=' ')
    i -= 1
print("\n")

# 3. Triangle
print("3. Triangle:")
for i in range(1, 8):
    print('#' * i)
print()

# 4. Grille
print("4. Grille:")
for i in range(5):
    print('# ' * 13)
print()

# 5. Table de multiplication
print("5. Table de multiplication:")
for i in range(11):
    print(f"{i} x {i} = {i*i}", end='  ')
print("\n")

# 6. Itération de liste
print("6. Itération de liste:")
liste = ["python", "numpy", "pandas", "django", "flask"]
for element in liste:
    print(element, end=' ')
print("\n")

# 7. Nombres pairs de 0 à 100
print("7. Nombres pairs de 0 à 100:")
for i in range(0, 101, 2):
    print(i, end=' ')
print("\n")

# 8. Nombres impairs de 0 à 100
print("8. Nombres impairs de 0 à 100:")
for i in range(1, 101, 2):
    print(i, end=' ')
print("\n")

# Niveau 2

# 1. Somme de tous les nombres
print("Niveau 2 - 1. Somme de tous les nombres:")
total = 0
for i in range(101):
    total += i
print(f"La somme de tous les nombres est {total}\n")

# 2. Somme des pairs et impairs
print("2. Somme des pairs et impairs:")
somme_pairs = 0
somme_impairs = 0

for i in range(101):
    if i % 2 == 0:
        somme_pairs += i
    else:
        somme_impairs += i

print(f"Somme des pairs: {somme_pairs}")
print(f"Somme des impairs: {somme_impairs}\n")

# Niveau 3

# 1. Pays avec "land" (exemple)
print("Niveau 3 - 1. Pays avec 'land':")
countries = ["Finland", "Iceland", "Ireland", "Poland", "Switzerland"]
pays_avec_land = [pays for pays in countries if "land" in pays.lower()]
print(pays_avec_land)
print()

# 2. Inverser liste de fruits
print("2. Inverser liste de fruits:")
fruits = ["banane", "orange", "mangue", "citron"]
fruits_inverse = []
for fruit in reversed(fruits):
    fruits_inverse.append(fruit)
print(fruits_inverse)
print()

# 3. Données pays (exemple simplifié)
print("3. Données pays (exemple simplifié):")
country_data = [
    {"name": "Pays1", "languages": ["fr", "en"], "population": 10000000},
    {"name": "Pays2", "languages": ["en", "es"], "population": 50000000},
    {"name": "Pays3", "languages": ["fr"], "population": 20000000}
]

# i. Nombre total de langues
langues = set()
for pays in country_data:
    langues.update(pays.get("languages", []))
print(f"i. Nombre total de langues: {len(langues)}")

# ii. 10 langues les plus parlées (exemple simplifié)
from collections import defaultdict
langue_counts = defaultdict(int)

for pays in country_data:
    for langue in pays.get("languages", []):
        langue_counts[langue] += pays.get("population", 0)

top_10 = sorted(langue_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nii. 10 langues les plus parlées:")
for langue, count in top_10:
    print(f"{langue}: {count} locuteurs")

# iii. 10 pays les plus peuplés (exemple simplifié)
pays_tries = sorted(country_data, key=lambda x: x.get("population", 0), reverse=True)[:10]
print("\niii. 10 pays les plus peuplés:")
for i, pays in enumerate(pays_tries, 1):
    print(f"{i}. {pays['name']}: {pays['population']} habitants")