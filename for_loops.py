# Looping

# Looping is different depending on the language, yet most of them use a For Loop.

# A For Loop is where you define an iterator number and then cycle through data (list or dictionary, generally speaking) `foreach` entry in that data structure.
# Creating a For Loop

list_data = [1, 2, 3, 4, 5, 6]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num(enumerate = each item in the list_data)
# num (can be called anything)- needs to be a variable = every entry within the list
# for num in list_data:
#     print(num * 2) # prints 2, 4, 6, 8, 10, 12 - as it goes on a loop throughout the list, takes each entry in the list, and performs the action mentioned, which in this case is "*2".

# best practice is to use "num" or a placeholder for the data in the list (that makes sense depending on the data types within the list).

# nested for loops(for loop within a for loop):
# for data in embedded_lists:
#     print(data) # Gives access to data in the main list. # print(data) = data in a list
#     for num in data:
#         print(num) # Gives access to the data within the embedded lists.

# for num in dict_data:
#     print(num) # prints the names of the dictionaries embedded in the main dictionary
#
# for item in dict_data.values():
#     print(item) # prints the value assigned to each embedded dictionary within the main dictionary variable.
#     for embed_value in item.values():
#         print(embed_value) # prints the embedded values within each dictionary in the main dictionary - does not print out the keys, as we only asked for the values, which in dictionaries, are the data on the right.

# MAKE SURE THE INDENTATION IS ALWAYS CORRECT!!!

# for items in dict_data.values():
#     print(items["money"]) # in this way we can access the values from only a certain key within the dictionaries.


# Please see Python documentation for more of what you can do with dictionaries and loops.


# Loops and if statements.

list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")

# Iterates through each item in the list, based on the conditions, and depending on which condition it fulfills, it prints the statement assigned as a result of fulfilling the specific condition.

