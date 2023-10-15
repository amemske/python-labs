
def countdown(n):
    if n <= 0:
        print ('Blastoff')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        print ('Blastoff')
    else:
        print(n)
        countup(n+1)


value = int(input("Please enter a number: "))

if value < 0:
    countup(value)
elif value > 0:
    countdown(value)
else: # when the value is zero
    countdown(value)