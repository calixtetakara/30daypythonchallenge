from functools import reduce
from collections import Counter

# Sample data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Alice', 'Bob', 'Charlie']
numbers = [1, 2, 3, 4, 5, 6, 7]

# LEVEL 1

# 1. Difference between map, filter, reduce
# map: transforms items
# filter: selects items based on condition
# reduce: aggregates items into one value

# 2. Difference between higher-order function, closure, decorator
# Higher-order: takes/returns functions
# Closure: remembers outer scope variables
# Decorator: modifies function behavior

# 3. Define a call function before map/filter/reduce
def square(x):
    return x * x

squared = list(map(square, numbers))

# 4. Print each country
for country in countries:
    print(country)

# 5. Print each name
for name in names:
    print(name)

# 6. Print each number
for number in numbers:
    print(number)

# LEVEL 2

# 1. Map: countries to uppercase
upper_countries = list(map(str.upper, countries))

# 2. Map: numbers to square
squared_numbers = list(map(lambda x: x**2, numbers))

# 3. Map: names to uppercase
upper_names = list(map(str.upper, names))

# 4. Filter: countries containing 'land'
land_countries = list(filter(lambda x: 'land' in x, countries))

# 5. Filter: countries with exactly 6 characters
six_char_countries = list(filter(lambda x: len(x) == 6, countries))

# 6. Filter: countries with 6+ letters
six_or_more = list(filter(lambda x: len(x) >= 6, countries))

# 7. Filter: countries starting with 'E'
starts_with_e = list(filter(lambda x: x.startswith('E'), countries))

# 8. Chain map → filter → reduce
chained_result = reduce(lambda x, y: x + y,
                        filter(lambda x: x > 10,
                               map(lambda x: x * 2, numbers)))

# 9. Function to get string items
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

# 10. Reduce: sum numbers
total_sum = reduce(lambda x, y: x + y, numbers)

# 11. Reduce: concatenate countries into sentence
sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + \
           f", and {countries[-1]} are north European countries"

# 12. Categorize countries by pattern
def categorize_countries(pattern):
    return list(filter(lambda x: pattern in x, countries))

# 13. Dictionary of starting letters
def country_initials_count(countries):
    return dict(Counter([country[0] for country in countries]))

# 14. First ten countries
def get_first_ten_countries(countries):
    return countries[:10]

# 15. Last ten countries
def get_last_ten_countries(countries):
    return countries[-10:]

# LEVEL 3 (requires countries_data.py)
# Assuming 'data' is a list of dictionaries from countries_data.py

# Example structure:
# data = [
#     {'name': 'Finland', 'capital': 'Helsinki', 'population': 5500000, 'languages': ['Finnish', 'Swedish']},
#     ...
# ]

# 1. Sort by name, capital, population
def sort_countries(data):
    by_name = sorted(data, key=lambda x: x['name'])
    by_capital = sorted(data, key=lambda x: x['capital'])
    by_population = sorted(data, key=lambda x: x['population'], reverse=True)
    return by_name, by_capital, by_population

# 2. Top 10 most spoken languages
def top_languages(data):
    all_languages = [lang for country in data for lang in country['languages']]
    return Counter(all_languages).most_common(10)

# 3. Top 10 most populated countries
def top_populated_countries(data):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:10]
