# While Loops

# Not as common as for loops
# Quite simple, but can be damaging if not understood properly

# While Loop = monitors data instead of iterating data

# Showcasing
#x = 0

# while x < 10:
#     print(f"it`s working! -> {x}")
    # x += 1 # incrementer
    # repeats the process of adding the incrementer and printing out until it gets to 10 (fulfills the while condition), and then it stops = monitoring.

# While loops always need to have a **break**, otherwise they can go on and on.

# while x < 10:# reasoning; comparison criteria
#     print(f"it`s working! -> {x}")
#     if x == 4:
#         break
#     x += 1
#
# print(x) # will print 4, as the break takes you out completely of the while loop!


# Using while loops to verify use input

# Asking for someone`s age
# This can either be an int (20) or a string (twenty)
# age = input("What is your age?")
#
# print(f"Your age is {age}.")

# user_prompt = True
#
# while user_prompt:
#     age = input("What is your age?")
#     if age.isdigit():
#         user_prompt = False
#     else:
#         print("Please provide your answer in digits.")
#
# print(f"Your age is {age}.")

# user_prompt = True
#
# while user_prompt:
#     age = input("What is your age?")
#     if age.isdigit() and int(age) < 117:
#         user_prompt = False
#     else:
#         print("Please provide your answer in digits and below 117.")
#
# print(f"Your age is {age}.")