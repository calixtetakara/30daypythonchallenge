# Jour 2: 30 Days of Python Programming

# 3. Déclaration d'une variable de prénom
first_name = "Calixte"

# 4.  Déclaration d'une variable de nom de famille
last_name = "TAKARA"

# 5.  Déclaration d'une variable de nom complet
full_name = "Calixte TAKARA"

# 6.  Déclaration d'une variable de pays
country = "Togo"

# 7.  Déclaration d'une variable municipale (ville)
city = "Kara"

# 8.  Déclaration d'une variable d'âge
age = 18 

# 9.  Déclaration d'une variable est_Married (est marié)
is_married = False

# 10.  Déclaration d'une variable is_true
is_true = True

# 11.  Déclaration d'une variable is_light_on
is_light_on = False

# 12.  Déclaration de plusieurs variables sur une seule ligne
var1, var2, var3 = 10, "Hello", True
# 13.  Déclaration d'une année
annee=2025
# ============================Exercic2==========================
# 1. Vérifier le type de données des variables
print(type(first_name))    # <class 'str'>
print(type(last_name))     # <class 'str'>
print(type(full_name))     # <class 'str'>
print(type(country))       # <class 'str'>
print(type(city))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(is_married))    # <class 'bool'>
print(type(is_true))       # <class 'bool'>
print(type(is_light_on))   # <class 'bool'>

# 2. Longueur du prénom avec len()
print(len(first_name))     # Exemple : 4 (si first_name = "Jean")

# 3. Comparaison des longueurs prénom/nom
print(len(first_name) > len(last_name))  # True ou False

# 4. Déclaration de num_one et num_two
num_one = 5
num_two = 4

# 5. Addition
sum = num_one + num_two                  # 9
print(sum)

# 6. Soustraction
difference = num_one - num_two           # 1
print(difference)

# 7. Multiplication
product = num_one * num_two              # 20
print(product)

# 8. Division
division = num_one / num_two             # 1.25
print(division)

# 9. Modulo
remainder = num_two % num_one            # 4 (car 4/5 = 0 reste 4)
print(remainder)

# 10. Division entière (Floor Division)
floor_division = num_one // num_two      # 1 (5//4 = 1.25 → arrondi à 1)
print(floor_division)
# 11-Récupération des données utilisateur
first_name = input("Prénom : ")
last_name = input("Nom : ")
country = input("Pays : ")
age = int(input("Âge : "))  # Conversion en entier

print(f"Merci, {first_name} {last_name} !")
#Calculs géométriques (cercle)
import math

radius = 30
# i. Aire du cercle
area_of_circle = math.pi * radius ** 2   # ≈ 2827.43
print(area_of_circle)

# ii. Circonférence
circum_of_circle = 2 * math.pi * radius  # ≈ 188.50
print(circum_of_circle)

# iii. Avec entrée utilisateur
radius = float(input("Entrez le rayon (m) : "))
area_user = math.pi * radius ** 2
print(f"Aire : {area_user:.2f} m²")
