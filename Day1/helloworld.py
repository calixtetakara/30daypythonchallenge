# ===================Exercice 2====================
# Numéro 2
print(3 +4) #L'addition
print(3-4) #Soustraction
print(3*4) #multiplication
print(3%4) #Modulo
print(3/4) #Division
print(3**4) #expo
print(3//4) #floor division 


# Numéro 3
print('''O Calixte o TAKARA
o TOGO o je profite de 30 jours
de python''')


# Numéro 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4))
print(type(4-4J))
print(type(['Asbeneh', 'Python', 'Finlande']))
print(type(('''O Calixte o TAKARA
o TOGO o je profite de 30 jours
de python''')))

# =================Exercice3===================

# Numéro 1
print(1) #int
print(55.68) # float
print(859 + 4j) #Nombrecomplexe
print('Je suis ravi de  prendre part à ce challenge') # chaine de charactère
print(True) # Boolean
print([12,856,85,23]) # List
print({'Nom':'TAKARA', 'prenom':'Calixte'}) # Dictionnary
print(('Calixte will become good','after 30 days', 'at python', 'am the best','God help me')) # Tuple
print({35,58.25,8})# set

# Numéro 2

import math as np

point1 = np.array([2, 3])
point2 = np.array([10, 8])

distance = np.linalg.norm(point2 - point1)

print(f"Distance euclidienne : {distance}")  # Output identique