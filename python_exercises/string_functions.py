# length
a = "My First String"
print(len(a))  # 15

# concatinate
b = "Happy place"
c = "Nursery School"

name = b + c
print(name)  # Happy placeNursery School

# slip into a list

splitText = b.split(' ')  # split where we have a space
print(splitText)  # ['Happy', 'place']

splitText2 = b.split('a')  # split where we have a letter 'a'
print(splitText2)  # ['H', 'ppy pl', 'ce']

# find a string position

found_string = c.find('l')
print(found_string)  # 13

# replace strings
replaced_string = c.replace('o', 'e')
print(replaced_string)  # Nursery Scheel

# evaluate
f = '2+6*4'
print(f)  # 2+6*4

print(eval(f))  # 26
