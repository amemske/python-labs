# Tuples are immutable unlike lists

emp = ()

print(type(emp))

city = ("nairobi", "Kisumu", "Mombasa")
print(type(city))

# difference between lists and tuples
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)

list1.append(5)
print(list1)  # [1, 2, 3, 4, 5]

# tuple1.append(5)
# print(tuple1) #AttributeError: 'tuple' object has no attribute 'append'

# concatenation
print(city + tuple1)  # ('nairobi', 'Kisumu', 'Mombasa', 1, 2, 3, 4)

# get last item
print(city[-1])  # Mombasa

# get an item at an index

print(city[1])  # Kisumu

# nesting
nest = (city, tuple1)
print(nest)  # (('nairobi', 'Kisumu', 'Mombasa'), (1, 2, 3, 4))

# repetition
rep = ("python",) * 5
print(rep)  # ('python', 'python', 'python', 'python', 'python')

rep2 = ("rocks",)
print(rep2 * 3)

# slice
list2 = (2, 4, 6, 8, 10)
print(list2[3:])  # (8, 10)

# slice reverse
print(list2[::-1])  # (10, 8, 6, 4, 2)

# unpacking


# deleting
print(list1)
del list1

# print(list1)  # NameError: name 'list1' is not defined.

# built-in functions

num1 = (2, 3, 4, 4, 4, 8, 6, 6, 1)

# count - occurrences
print(num1.count(6))  # 2

# max
print(max(num1))  # 8

# min
print(min(num1))  # 1

# len
print(len(num1))  # 9

# sum
print(sum(num1))  # 28

# converting lists to tuples
list3 = ["one", "two", "three"]

print(list3)  # ['one', 'two', 'three']

# convert list to tuple
listToTuple = tuple(list3)
print(listToTuple)  # ('one', 'two', 'three')

# nesting tuples in a list
list_of_tuples = [(1, 2, 3), (9, 7, 5)]
print(list_of_tuples)  # [(1, 2, 3), (9, 7, 5)]

list_of_tuples.append(("five", "nine", "eight"))
print(list_of_tuples)  # [(1, 2, 3), (9, 7, 5), ('five', 'nine', 'eight')]

tuple_of_lists = ([1, 2, 3], ["a", "b", "c"])
print(tuple_of_lists)  # ([1, 2, 3], ['a', 'b', 'c'])
tuple_of_lists[0].append("z")

print(tuple_of_lists)  # ([1, 2, 3, 'z'], ['a', 'b', 'c'])

tuple_of_lists[0].remove("z")
print(tuple_of_lists)  # ([1, 2, 3], ['a', 'b', 'c'])

# Adding to a tuple
series = (0, 1, 2, 3, 4, 5)
series1 = series + (6,)
print(series1)  # (0, 1, 2, 3, 4, 5, 6)

# add series 1 + the reverse of series
series2 = series1 + series[:: -1]
print(series2)  # (0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0)
