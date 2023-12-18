grades = {"Antony": 90, "Mary": 85}
print(grades['Antony'])  # 90
print(grades)  # 90

# check if value exists
print('Mary' in grades)  # True
print('Susan' in grades)  # False

# get dictionary keys
allKeys = grades.keys()
print(allKeys)  # dict_keys(['Antony', 'Mary'])

# convert dict keys to list
print(list(allKeys))  # ['Antony', 'Mary']

# convert dict values to list
allValues = grades.values()
print(allValues)  # dict_values([90, 85])

allValuesList = list(allValues)
print(allValuesList)  # [90, 85]

# count values
print(allValuesList.count(85))  # 1

# add to a dictionary
grades['Mathew'] = 80
print(grades)  # {'Antony': 90, 'Mary': 85, 'Mathew': 80}

# another way to create a dictionary

person = dict(name="Jessy", age=27, height="6ft")
print(person)  # {'name': 'Jessy', 'age': 27, 'height': '6ft'}

print(person.items())  # dict_items([('name', 'Jessy'), ('age', 27), ('height', '6ft')])
