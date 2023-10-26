# Using zip() with Lists: You can use the zip() function to combine data from multiple lists into tuples by creating
# tuples with elements at the same index
# Here is an example

teams = ['Manchester United', 'Arsenal', 'Liverpool']
points = [52, 66, 70]

for teams, points in zip(teams, points):
    print(f"{teams} : points {points}")

# output ------------------
# Manchester United : points 52
# Arsenal : points 66
# Liverpool : points 70

# Using enumerate() with Lists: it returns a tuple where the first element is the index or position of the element in
# the iterable, and the second element is the value of the element itself.

cars = ['audi', 'bmw', 'suzuki', 'vw']

for index, car in enumerate(cars, start=1):
    print(f"Car no. {index} is {car}")

# output ------------------

# Car no. 1 is audi
# Car no. 2 is bmw
# Car no. 3 is suzuki
# Car no. 4 is vw


# Using items() with Dictionaries:the items() method provides key-value pairs as tuples.
# This allows you to easily loop through both the keys and values of the dictionary.
# Here is an example

staff1 = {
    'id': '3453',
    'name': 'John Doe',
    'age': 32,
    'occupation': 'Game Developer'
}

for key, value in staff1.items():
    print(f"{key}: {value}")

# output -----------------
# id: 3453
# name: John Doe
# age: 32
# occupation: Game Developer
