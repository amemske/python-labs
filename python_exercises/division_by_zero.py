valueOne = int(input("Enter first number: "))
valueTwo = int(input("Enter second number: "))

if  valueOne == 0 or valueTwo == 0:
    print('Division with zero is not allowed')
else:
    result = valueOne / valueTwo
    print(result)