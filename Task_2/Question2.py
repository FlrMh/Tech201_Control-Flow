# Odd/Even

# Ask user for a number;
# If the number is odd - print(The number is odd!)
# If the number is even - print(The number is even!)

number_choice = int(input("Please, type a number."))


if (number_choice % 2) == 0:
    print("This number is even!")
else:
    print("This number is odd!")
