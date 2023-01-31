# Loops and lists task

# 1. Make a loop with a range that says hello 10 times.

greeting_statement = "Hello!"
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in x:
    if num <= 10:
        print("Hello!")


# 2. Make a loop with a range that asks for names and appends to list_names.

list_names = ["Diana", "Sonia", "Michaela"]

user_name = str.capitalize(input("Please, insert your name:"))

for value in user_name:
    list_names.append(user_name)
    break

print(list_names)


# 3. Make a loop that iterates over each name in list_name and formats it into lowercase in a new variable called list_names_lower.




