# Control Flows

# Control flow - flow through a particular decision process (e.g. In a supermarket: if I can find a smaller queue at a cashiery, I will go to that one);
# You can use them by themselves or use them together

# if_statement

# showcasing
# age = 19

# if age > 18: # either > or >=
#     print("You are the correct age to watch this movie and can buy a ticket.") #clause
# if age < 18:
#     print("Unfortunately, you are not the correct age to watch this movie, and therefore, cannot buy a ticket.")

# Having separate if statements can be hard to understand/follow in a complex code
# Here is where we can use elif and else:

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

# In Python, there are no `switch statements` or `case statements`, which you would see in other languages.

