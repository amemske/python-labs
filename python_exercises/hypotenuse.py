# incremental development - write small code test it out before you move on
import math


def hypotenuse(a, b):
    # calculate squares of a and b
    a_squared = a ** 2
    b_squared = b ** 2
    print(f' the square of a is {a_squared} and that of b is {b_squared}')

    # Add the square roots to get c squared
    c_squared = a_squared + b_squared
    print(f' the sum of a_squared + b_squared is {c_squared}')

    # get the square root to find the hypotenuse
    result = math.sqrt(c_squared)
    print(f'the hypotenuse is {result} which is the square root of c_squared')

    return result

print(hypotenuse(3, 4))
# Output 5.0

print(hypotenuse(5, 6))
# Output 7.8

print(hypotenuse(4, 2))
# Output 4.4

print(hypotenuse(9, 18))
# Output 20.1
