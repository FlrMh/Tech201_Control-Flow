# ***Tech201-Control Flow***
An introduction to Control Flow in Python.

There comes situations in real life when we need to make some decisions and based on these decisions, we decide what should we do next. Similar situations arise in programming also where we need to make some decisions and based on these decisions we will execute the next block of code. 

**Decision-making statements** in programming languages decide the direction of the flow of program execution. 

- In Python, `if`, `elif`, `else` statements are used for **decision-making**.

##  If Statements

`if statement` is *the most simple* **decision-making statement**. 

- It is used to **decide** whether a certain *statement or block of statements* will be *executed or not*.

```bash
# showcasing
age = 19

if age > 18: # either > or >=
     print("You are the correct age to watch this movie and can buy a ticket.") #clause
if age < 18:
     print("Unfortunately, you are not the correct age to watch this movie, and therefore, cannot buy a ticket.")
```
- Having separate if statements can be hard to understand/follow in a complex code
- Here is where we can use `elif` and `else`:
```bash
film_rating = "16"

if film_rating.lower() == "universal":
    print("All age groups can watch this film.")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance advised.")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12. Supervision is recommended.")
elif film_rating.lower() == "15":
    print("You must be 15 to watch 15 rated movies in cinema.")
elif film_rating.lower() == "18":
    print("You must be 18 to watch 18 rated movies in cinema.")
else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")
# Hard-coded code (no user input allowed)
```
- `else` statements catch everything else if the criteria was not met. 

- They will be executed if all the conditions under `if` and `elif` statements are `False`.

!!! In Python, there are no `switch statements` or `case statements`, which you would see in other languages. 

## 2. For Loops

In programming, the **loops** are the constructs that *repeatedly execute a piece of code based on the conditions*. These are useful in many situations like going through every element of a list, doing an operation on a range of values, etc.

Looping is different depending on the language, yet most of them use a **For Loop**.

- A **For Loop** is where you *define an iterator number* and then *cycle through data* (list of dictionary, generally speaking) `for` each entry in that data structure.

a. Creating a For Loop
```bash
list_data = [1, 2, 3, 4, 5, 6]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num (variable = each item in the list_data).
# num (can be called anything)- needs to be a variable.
for num in list_data:
    print(num * 2) # prints 2, 4, 6, 8, 10, 12 - as it goes on a loop throughout the list, takes each entry in the list, and performs the action mentioned, which in this case is "*2".

# best practice is to use "num" or a placeholder for the data in the list (that makes sense depending on the data types within the list).
```

b. Understanding Nested For loops (For Loop within a For Loop):
```bash
for data in embedded_lists:
    print(data) # Gives access to data in the main list. # print(data) = data in a list
    for num in data:
         print(num) # Gives access to the data within the embedded lists.

 for num in dict_data:
     print(num) # prints the names of the dictionaries embedded in the main dictionary

 for item in dict_data.values():
     print(item) # prints the value assigned to each embedded dictionary within the main dictionary variable.
     for embed_value in item.values():
         print(embed_value) # prints the embedded values within each dictionary in the main dictionary - does not print out the keys, as we only asked for the values, which in dictionaries, are the data on the right.


# !!! MAKE SURE THE INDENTATION IS ALWAYS CORRECT!!!

 for items in dict_data.values():
     print(items["money"]) # in this way we can access the values from only a certain key within the dictionaries.
```

*Please see Python documentation for more of what you can do with dictionaries and loops.


c. Combining Loops and If statements.
```bash
list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")

# Iterates through each item in the list, based on the conditions, and depending on which condition it fulfills, it prints the statement assigned as a result of fulfilling that specific condition.
```


## 3. While Loops

**While Loops** are not as common as For Loops. They are *quite simple*, but can be *damaging for a programme if they are not understood and used properly*.

- **While loops** *execute* a set of lines of code *iteratively* *till a condition is satisfied*. Once the *condition results in False*, it **stops execution**, and the part of the program after the loop starts executing.

- While Loop = monitors data instead of iterating data

Let`s showcase a While Loop:
```bash
x = 0

while x < 10:
     print(f"it`s working! -> {x}")
     x += 1 # incrementer
    # repeats the process of adding the incrementer and printing out until it gets to 10 (fulfills the while condition), and then it stops = monitoring.
```
- While loops always need to have a **break**, otherwise they can go on and on.

Let`s showcase the use of a break:
```bash
 while x < 10:# reasoning; comparison criteria
     print(f"it`s working! -> {x}")
     if x == 4:
         break
     x += 1

 print(x) # will print 4, as the break takes you out completely of the while loop!
```

-  Using while loops to verify use input

Let`s showcase this in a programme that is asking for someone's age:
```bash
# Age can either be an int (20) or a string (twenty)
 age = input("What is your age?")

 print(f"Your age is {age}.")

 user_prompt = True

 while user_prompt:
     age = input("What is your age?")
     if age.isdigit():
         user_prompt = False
     else:
         print("Please provide your answer in digits.")

 print(f"Your age is {age}.")
```
```bash
 user_prompt = True

 while user_prompt:
     age = input("What is your age?")
     if age.isdigit() and int(age) < 117:
         user_prompt = False
     else:
         print("Please provide your answer in digits and below 117.")

 print(f"Your age is {age}.")
```