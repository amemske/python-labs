# Recursive function to calculate the sum of all positive integers from 1 to n

def sum_of_numbers(n):
    if(n==1):
        return 1
    else:
        return n + sum_of_numbers(n -1)

print(sum_of_numbers(5))