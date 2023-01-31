# Guessing game

# Number variable 1-20
# 3 chances
# Give them a clue each time (go higher/ lower)
# Mention if the quess is not between the set variable
# Bonus: make the guess random each time they play.


# import random
# random_number = random.randint(1,20)
# win = False
# Turns = 3


# x = (1, 20)
# win = False
#
# for num in x:
#     if num == 5:
#         print("You guessed it! Congratulation!")
#         win == True
#         break
#     elif num > 5:
#         print("Your guess was too high. Please enter a lower number.")
#     else:
#         print("Your guess was too low. Please enter a higher number.")


num = 5
attempts = 2
msg = "You lost!"

while attempts > 0:
    user_input = int(input("Enter a number between 1 and 20:"))
    if user_input == num:
        msg = "You Won!"
        break
    elif user_input > 5:
        print(f"You guess was too high! Try again! {attempts} attempts left.")
        attempts -= 1
    elif user_input < 5:
        print(f"Your guess was too low! Try again! {attempts} attempts left")
        continue

print(msg)

