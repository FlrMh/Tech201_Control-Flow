# Improved movie rating program

# user_prompt = True
# while user_prompt:
#     age = input("What is your age?")
#     if age.isdigit() and int(age) < 117 and int(age) > 1:
#          user_prompt = False
#     else:
#          print("Please provide your answer in digits and below 117.")
#
# print(f"Your age is {age}.")
#
# if int(age) >= 2:
#     print("You can watch movies rated as -Universal-.")
# elif int(age) >= 18:
#     print("You can watch movies rated as suitable only for adults.")
# elif int(age) >= 12 and int(age) < 15:
#     print("You can watch movies rated with -12- and -12A-.")
# elif int(age) <18 and int(age) >= 15:
#     print("You can watch movies rated with -12-, -12A- and -15-.")
# else:
#      print("This is not a correct rating, please use universal, pg, 12, 15, 18")

# Define your functions

# def over_18(age):
#     print(f"Your age is {age}, therefore, you can watch -A18- and -Universal- rated movie.")
#
# def between_18_15(age):
#     print(f"Your age is {age}, therefore, you can watch -15-, -12A-, -12- and -Universal- rated movies.")
#
# def between_12_15(age):
#     print(f"Your age is {age}, therefore, you can watch -12A-, -12-, and -Universal- rated movies.")
#
# def under_12(age):
#     print(f"Your age is {age}, therefore, you can watch -Universal- rated movies.")
#
# age = int(input("How old are you? "))
# if age >= 18:
#     print(over_18(age))
# elif age >= 15 and age < 18:
#     print(between_18_15(age))
# elif age >=12 and age < 15:
#     print(between_12_15(age))
# else:
#     print(under_12(age))


# Attempt #2

# Creating our function:

def check_age(age):
    if age.isdigit() and -1 < int(age) < 117:
        if int(age) < 12:
            return "You can watch Universal and PG rated movies."
        elif 12 <= int(age) < 15:
            return "You can watch 12, 12A and Universal rated movies."
        elif 14 < int(age) < 18:
            return "You can watch Universal, 12, 12A and 15 rated movies."
        else:
            return "You can watch all types of movies."
    else:
        age = input("What is your age? Please, introduce it in digits.")
        check_age(age)

age = input("What is your age?")
print(check_age(age))