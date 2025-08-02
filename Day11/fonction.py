import math
from collections import Counter

# Niveau 1
def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r ** 2

def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Tous les éléments doivent être des nombres"
        total += num
    return total

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(month):
    if month in [12, 1, 2]:
        return "hiver"
    elif month in [3, 4, 5]:
        return "printemps"
    elif month in [6, 7, 8]:
        return "été"
    else:
        return "automne"

def calcul_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Pas de solution réelle"
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (x1, x2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(arr):
    return arr[::-1]

def capitalize_list_items(lst):
    return [item.upper() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n+1))

def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

# Niveau 2
def evens_and_odds(n):
    evens = n // 2 if n % 2 == 0 else (n // 2) + 1
    odds = n // 2
    return f"Pairs: {evens}, Impairs: {odds}"

def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

def is_empty(param):
    return not bool(param)

def calculate_mean(lst):
    return sum(lst)/len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    return (sorted_lst[n//2] if n % 2 else (sorted_lst[n//2-1] + sorted_lst[n//2])/2)

def calculate_mode(lst):
    return Counter(lst).most_common(1)[0][0]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x-mean)**2 for x in lst)/len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

# Niveau 3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_unique(lst):
    return len(lst) == len(set(lst))

def same_data_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

def is_valid_variable(name):
    import keyword
    return name.isidentifier() and not keyword.iskeyword(name)

def most_spoken_languages(data, n=10):
    languages = {}
    for country in data:
        for lang in country['languages']:
            languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:n]

def most_populated_countries(data, n=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:n]