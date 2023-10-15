# generate lists
my_range1 = range(6)
my_range2 = range(1, 7)
my_range3 = range(0, 8, 2)  # skip by 2

print(list(my_range1))  # [0, 1, 2, 3, 4, 5]
print(list(my_range2))  # [1, 2, 3, 4, 5, 6]
print(list(my_range3))  # [0, 2, 4, 6]

# for loop using rabge
for i in range(10):
    print(i)

# 0,1,2,3,4,5,6,7,8,9

# get the sum

totalSum = 0
for i in range(10):
    totalSum = totalSum + i

print(totalSum)  # 45


# countdown using while loop
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')


countdown(5)

# A string is a sequence of characters
fruit = 'banana'
letter = fruit[1]
print(letter)

# length
phrase = 'money talks'
print(len(phrase))  # 11

length = len(phrase)

last = phrase[length - 1]
print(last)  # s

# transverse a string
index = 0
while index < len(phrase):
    letter = phrase[index]
    print(letter)
    index = index + 1

# transverse a string and append
prefixes = 'JKLM'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)  # Jack, Kack, Lack, Mack


# searching
def find(word, letter):
    i = 0
    while i < len(word):
        if word[i] == letter:
            return i
        i = i + 1
    return -1


# looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# compare strings
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            return letter


result = in_both('tony', 'money')
print(result)


# compare strings alternative option
def in_both(word1, word2):
    common_letters = []
    for letter in word1:
        if letter in word2:
            common_letters.append(letter)
    return common_letters


result = in_both('tony', 'money')
print(result)

# slice strings

s = 'Monty Python'
print(s[0:5])  # Monty

fruit = 'apples'
print(fruit[:3])  # app

print(fruit[3:])  # les

print(fruit[:])  # apples
