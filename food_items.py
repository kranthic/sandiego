__author__ = 'kranthi'

import pymongo


food_items = []
while True:
    food_item = {}
    name = raw_input('Enter the name of the food item (hit enter to exit) ')
    if len(name) == 0:
        break

    food_item['name'] = name

    synonymns = []
    syn = raw_input('Enter synonymn (hit enter to exit this question) ')
    while not len(syn) == 0:
        synonymns.append(syn)
        syn = raw_input('Enter synonymn (hit enter to exit this question) ')

    food_item['synonymns'] = synonymns
    food_items.append(food_item)

print food_items
