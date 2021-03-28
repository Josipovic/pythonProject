friends = {'tom': 'cat',
           'jerry': 'mouse'}

print(friends)

# retrieving elements from the dictionary
print(friends['tom'])

# adding elements to the dictionary
friends['bob'] = 'giraffe'

# modify elements in the dictionary
friends['bob'] = 'dog'

# delete elements in the dictionary
del friends['bob']

# looping items in the dictionary

alphabet = {'A': '100', 'B': '200', 'C': '300', 'D': '400'}

for x in alphabet:
    print(x, ":", alphabet[x])

# equality test in dictionary
d1 = {'MIKE': 41, 'BOB': 22}
d2 = {"BOB": 22, 'MIKE': 41}

print(d1 == d2)
print(d1 != d2)

# dictionary methods

# popitem() returns randomly selected item from dictionary and also removes the selected item
print(friends.popitem())

# clear() delete everything from dictionary
# print(friends.clear())

# keys() return keys in dictionary as tuples
print(friends.keys())

# values() returns values in dictionary as tuples
print(friends.values())

# get(key)  return value of key
print(friends.get('tom'))

# pop(key) remove the item from the dictionary
# friends.pop('tom')

