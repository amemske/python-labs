# Write program to display your name and perform following operations on it
n = input("Enter your name: ")
print(n)
# Output
# Antony

# Display n characters from left - traverse
for letter in n:
    print(letter)

# output
# A
# n
# t
# o
# n
# y


# count the number of vowels by comparing the two strings
vowels = 'aeiou'
input_name_lowercase = n.lower()
count = 0


def compare_strings(passed_input, letters):
    global count  # Not strictly necessary here since 'count' is global by default
    for each_letter in passed_input:
        if each_letter in letters:
            count = count + 1


compare_strings(input_name_lowercase, vowels)
print(count)

# Output
# 2

# Reverse the name passed as input using slice

string_length = len(n)  # is 6, string length used as slicing index
slicedString = n[string_length::-1]
# -1 means the order is revered, start from the last character (6) and go backwards
print(slicedString)

# Output
# ynotnA
