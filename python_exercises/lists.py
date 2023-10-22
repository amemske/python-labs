a = [9, -7, 0, 0, 5, 10]

print(a[0])  # 9

a[4] = "this text"

print(a)  # [9, -7, 0, 0, 'this text', 10]

a[1] = [-6, -3]

print(a)  # [9, [-6, -3], 0, 0, 'this text', 10]

# c = b does not mean c is a copt of b, it means they are referring to the same thing
b = [7, 13, 15]
c = b

c[0] = 18

# they point to the same data
print(c)  # [18, 13, 15]
print(b)  # [18, 13, 15]

# copying a list
f = b[:]  # copy everything from the beginning until
print(f)  # [18, 13, 15]

# copy a few elements
g = b[0:1]
print(g)  # [18]

# multiply items in list
twos = [2] * 6
print(twos)  # [2, 2, 2, 2, 2, 2]

# combine lists
combined = g + twos
print(combined)  # [18, 2, 2, 2, 2, 2, 2]

# various ways to create a list
numbers = list(range(10))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

chars = list("Hello")
print(chars)  # ['H', 'e', 'l', 'l', 'o']

# get string length
print(len(chars))  # 5

# append
chars.append("Nice try")
print(chars)  # ['H', 'e', 'l', 'l', 'o', 'Nice try']

# list in reverse order

# list  as even numbers - 2 steps

# list unpacking into multiple variables

my_list = [1, 2, 3]
first, second, third = my_list

print(first)  # 1
# unpack only two items from a list

my_list2 = [2, 3, 4, 5, 8]
item1, item2, *other = my_list2

print(item1)  # 2
print(item2)  # 3
print(other)  # [4, 5, 8]


# you can also get the last - item item1, item2, *other, last = my_list2


# unpacking list in function example
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(1, 2, 3, 4, 5))  # 120

# use for loop with lists
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)  # a b c

# creatina a tuple(a list that is readonly and also has indexes)
for index, letter in enumerate(letters):
    print(index, letter)

# 0 a
# 1 b
# 2 c

# adding items
letters.append("d", "e", "f")
letters.insert(0, "-")
print(letters)

# removing items
letters.pop()  # removes last item
print(letters)

letters.pop(1)  # removes at index1
print(letters)

letters.remove("a")  # removes "a"
print(letters)

# delete a range of items
del letters[0:1]
print(letters)

#remove everything in the list
letters.clear()


#find index in alist


#in python you have to iterate lists with an index while in js you don't need to

