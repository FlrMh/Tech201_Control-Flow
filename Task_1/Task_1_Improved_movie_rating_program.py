# Improved movie rating program

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117 and int(age) > 1:
         user_prompt = False
    else:
         print("Please provide your answer in digits and below 117.")

print(f"Your age is {age}.")

if int(age) >= 2:
    print("You can watch movies rated as -Universal-.")
elif int(age) >= 18:
    print("You can watch movies rated as suitable only for adults.")
elif int(age) >= 12 and int(age) < 15:
    print("You can watch movies rated with -12- and -12A-.")
elif int(age) <18 and int(age) >= 15:
    print("You can watch movies rated with -12-, -12A- and -15-.")
else:
     print("This is not a correct rating, please use universal, pg, 12, 15, 18")