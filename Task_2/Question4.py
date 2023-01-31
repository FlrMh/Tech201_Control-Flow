# FitBuzz

# Program that prints numbers from 1-100
# For multiples of 3 - prints Fizz
# For multiples of 5 - prints Buzz
# For multiples of 3 and 5 - prints FizzBuzz

x = range(1, 100)

for num in x:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz!")
    elif num % 3 == 0:
        print("Fizz!")
    elif num % 5 == 0:
        print("Buzz!")
    else:
        print(num)