
#=======================Exercice1================================

# 1. Déclaration de mon âge comme variable entière
age = 18

# 2. Déclaration de ma  taille en tant que variable flottante
taille = 1.75  

# 3. Déclaration d'une  variable qui stocke un numéro complexe
nombre_complexe = 3 + 4j

# 4. Script pour calculer l'aire d'un triangle
print("Calcul de l'aire d'un triangle")
base = float(input("Entrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))
aire = 0.5 * base * hauteur
print(f"L'aire du triangle est : {aire}")

# 5.Script pour calculer le périmètre d'un triangle
print("Calcul du périmètre d'un triangle")
cote_a = float(input("Entrez la longueur du côté A : "))
cote_b = float(input("Entrez la longueur du côté B : "))
cote_c = float(input("Entrez la longueur du côté C : "))

perimetre = cote_a + cote_b + cote_c
print(f"Le périmètre du triangle est : {perimetre}")

# ===================Exercice2================================
# 6.
longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))

aire = longueur * largeur
perimetre = 2 * (longueur + largeur)

print(f"Aire = {aire}, Périmètre = {perimetre}")
# 7.

rayon = float(input("Entrez le rayon du cercle : "))

aire = 3.14* rayon ** 2
circonference = 2 * 3.14* rayon

print(f"Aire = {aire}, Circonférence = {circonference}")

# 8.
# Équation : y = 2x - 2
pente = 2
ordonnee_y = -2  # (quand x=0, y=-2)
ordonnee_x = 1    # (quand y=0, x=1 : 0 = 2x - 2 → x=1)

print(f"Pente = {pente}, Ordonnée à l'origine X = {ordonnee_x}, Ordonnée à l'origine Y = {ordonnee_y}")
# 9.
x1, y1 = 2, 2
x2, y2 = 6, 10

# Pente (m = (y2 - y1) / (x2 - x1))
pente = (y2 - y1) / (x2 - x1)

# Distance euclidienne (√((x2 - x1)² + (y2 - y1)²))
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"Pente = {pente}, Distance euclidienne = {distance}")
# 10.
pente_ex8 = 2
pente_ex9 = (10 - 2) / (6 - 2)  # = 2

print("Les pentes sont égales ?", pente_ex8 == pente_ex9)  # True
# 11.
def calculer_y(x):
    return x**2 + 6*x + 9

# Test avec différentes valeurs de x
for x in [-3, -2, -1, 0, 1]:
    y = calculer_y(x)
    print(f"x = {x} → y = {y}")

# Solution de y = 0 : x² + 6x + 9 = 0 → (x + 3)² = 0 → x = -3
print("La valeur de x qui annule y est x = -3")
# 12.
longueur_python = len("Python")
longueur_dragon = len("Dragon")

print(f"Python : {longueur_python}, Dragon : {longueur_dragon}")

# Comparaison Falsy (exemple : vérifier si les longueurs sont égales)
comparaison_falsy = longueur_python == longueur_dragon  # False (6 != 6 → en réalité True, donc choisissons autre chose)
comparaison_falsy = not longueur_python  # False (car len("Python") = 6 → not 6 = False)
print("Comparaison Falsy :", comparaison_falsy)
# 13.
print("'on' dans 'python' ET 'dragon' ?", ('on' in 'python') and ('on' in 'dragon'))  # True
# 14.
phrase = "I hope this course is not full of jargon."
print("'jargon' est dans la phrase ?", 'jargon' in phrase)  # True
# 15.
longueur = len("python")
en_float = float(longueur)
en_string = str(en_float)

print(f"Longueur : {longueur}, Float : {en_float}, String : {en_string}")
# 16.
nombre = int(input("Entrez un nombre : "))
est_pair = nombre % 2 == 0

print(f"{nombre} est pair ? {est_pair}")