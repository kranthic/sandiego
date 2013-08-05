__author__ = 'kranthi'

import re

f = open('/Users/kranthi/chicken_recipes.txt')

stopwords = [word.strip() for word in open('dictionaries/stopwords.txt').readlines()]
stopwords_chars = [char.strip() for char in open('dictionaries/stopwordchars.txt').readlines()]
ingredients_stopwords = [word.strip() for word in open('dictionaries/ingredientsstopwords.txt').readlines()]


def remove_stopwords_chars(data):
    return ''.join(c for c in data.lower() if c not in stopwords_chars)

def is_stop_word(word):
    return word.lower() in stopwords

def is_ingredient_stop_word(word):
    return word.lower() in ingredients_stopwords

def parse_ingredient(data):
    tokens = remove_stopwords_chars(data).split()
    tokens = [w.strip() for w in tokens if not is_stop_word(w) and not is_ingredient_stop_word(w)]

    return " ".join(tokens).strip()


new = True
recipes = []
recipe = {}
for l in f:
    if len(l.strip()) == 0:
        new = True
        continue

    if new:
        if len(recipe) != 0:
            recipes.append(recipe)
            recipe = {}

        new = False
        recipe['name'] = l.strip()
        recipe['ingredients'] = []
    else:
        ingredient = parse_ingredient(l.strip())
        if len(ingredient) != 0 and ingredient not in recipe['ingredients']:
            recipe['ingredients'].append(ingredient)


if len(recipe) != 0:
    recipes.append(recipe)

for r in recipes:
    print r
