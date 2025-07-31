# Niveau 1 - Exercice 1
print("\nNiveau 1 - Exercice 1")
age = int(input("Entrez votre âge: "))
if age >= 18:
    print("Vous êtes assez vieux pour apprendre à conduire.")
else:
    print(f"Vous avez besoin de {18 - age} ans de plus pour apprendre à conduire.")

# Niveau 1 - Exercice 2
print("\nNiveau 1 - Exercice 2")
my_age = 25  # Vous pouvez modifier cette valeur
your_age = int(input("Entrez votre âge: "))
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("Vous avez 1 an de plus que moi.")
    else:
        print(f"Vous avez {difference} ans de plus que moi.")
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("Vous avez 1 an de moins que moi.")
    else:
        print(f"Vous avez {difference} ans de moins que moi.")
else:
    print("Nous avons le même âge.")

# Niveau 1 - Exercice 3
print("\nNiveau 1 - Exercice 3")
a = int(input("Entrez numéro un: "))
b = int(input("Entrez numéro deux: "))
if a > b:
    print(f"{a} est supérieur à {b}")
elif a < b:
    print(f"{a} est inférieur à {b}")
else:
    print(f"{a} est égal à {b}")

# Niveau 2 - Exercice 1
print("\nNiveau 2 - Exercice 1")
score = int(input("Entrez votre score: "))
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 89:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
else:
    grade = "F"
print(f"Votre note est: {grade}")

# Niveau 2 - Exercice 2
print("\nNiveau 2 - Exercice 2")
month = input("Entrez un mois: ").lower()
if month in ["septembre", "octobre", "novembre"]:
    print("La saison est automne.")
elif month in ["décembre", "janvier", "février"]:
    print("La saison est hiver.")
elif month in ["mars", "avril", "mai"]:
    print("La saison est printemps.")
elif month in ["juin", "juillet", "août"]:
    print("La saison est été.")
else:
    print("Mois invalide.")

# Niveau 2 - Exercice 3
print("\nNiveau 2 - Exercice 3")
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Entrez un fruit: ").lower()
if new_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(new_fruit)
    print(f"Liste modifiée: {fruits}")

# Niveau 3 - Exercice 1
print("\nNiveau 3 - Exercice 1")
personne = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'Python', 'MongoDB'],
    'zipcode': '02210'
}

# Vérification des compétences
if 'skills' in personne:
    print("Compétences intermédiaires:", personne['skills'][len(personne['skills'])//2])
    
    # Vérification de Python
    if 'Python' in personne['skills']:
        print("La personne a des compétences en Python.")
    
    # Détermination du type de développeur
    skills_set = set(personne['skills'])
    if skills_set == {'JavaScript', 'React'}:
        print("Il est un développeur frontend.")
    elif skills_set.issuperset({'Node', 'Python', 'MongoDB'}):
        print("Il est un développeur backend.")
    elif skills_set.issuperset({'React', 'Node', 'MongoDB'}):
        print("Il est un développeur fullstack.")
    else:
        print("Titre inconnu")

# Vérification du statut marital et du pays
if personne['is_married'] and personne['country'] == 'Finland':
    print(f"{personne['first_name']} {personne['last_name']} vit en Finlande. Il est marié.")