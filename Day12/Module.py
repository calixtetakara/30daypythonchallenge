import random
import string

# Niveau 1
def random_user_id():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def user_id_gen_by_user():
    char_count = int(input("Nombre de caractères par ID: "))
    id_count = int(input("Nombre d'IDs à générer: "))
    
    characters = string.ascii_lowercase + string.digits
    ids = []
    for _ in range(id_count):
        ids.append(''.join(random.choice(characters) for _ in range(char_count)))
    return ids

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'RGB({r}, {g}, {b})'

# Niveau 2
def list_of_hexa_colors(num_colors=1):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        colors.append(color)
    return colors

def list_of_rgb_colors(num_colors=1):
    colors = []
    for _ in range(num_colors):
        colors.append(rgb_color_gen())
    return colors

def generate_colors(color_type, num_colors):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return []

# Niveau 3
def shuffle_list(input_list):
    shuffled = input_list.copy()
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)

# Tests
print("Random User ID:", random_user_id())
print("User IDs générés:", user_id_gen_by_user())  # Testez avec 5 puis 5
print("Couleur RVB:", rgb_color_gen())
print("Couleurs hexa:", list_of_hexa_colors(3))
print("Couleurs RVB:", list_of_rgb_colors(3))
print("Générer couleurs (hexa):", generate_colors('hexa', 3))
print("Générer couleurs (rgb):", generate_colors('rgb', 1))
print("Liste mélangée:", shuffle_list([1, 2, 3, 4, 5]))
print("Nombres uniques:", unique_random_numbers())