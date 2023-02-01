# Task 4

# Question 1

# x = input ("Please add a number:")
# x = int (x)
# total_number = x
#
# sum = 0
# while x >= 0:
#     sum += x
#     x -= 1
#
# average = sum / total_number
# print("Sum of", total_number , "using while loop", sum)
# print("average of", total_number, "using while loop", average)

# working (no average)

def add(itr):
  total = 0
  for n in range(itr):
    num = float(input("number:"))
    total += num
    print(total)
add(10)



# Question 2:

# x = 300
#
# while x < 301:
#     print (x)
#     x += 10
# print(x)

# working version:

print("Factors of 10:")
x = 0

while x <= 300:
    print(x, end=" ")
    x = x + 10





