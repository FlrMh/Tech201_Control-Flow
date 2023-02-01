# User worked hours task

# Ask for hours worked and rate of pay;
# Calculate gross pay for the week;
# Note: Pay over 40h is 1.5 x hour rate.

# print("Welcome to your income calculator!")
#
# hourly_rate = float(input("Please provide your hourly rate."))
#
#
# worked_hours = float(input("Please provide the amount of hours worked this week."))
# if worked_hours > 40:
#     overtime = worked_hours - 40
#     overtime_pay = overtime * (hourly_rate * 1.5)
#     gross_income = 40 * hourly_rate + overtime_pay
# else:
#     gross_income = worked_hours * hourly_rate
#
# print(f"Your gross income for this week, when you worked {worked_hours}, will be {gross_income}.")


# Version 2 using functions

# Approach the question logically. What do we need the program to do? = calculate income.
# income :
# 40h - normal income
# or over 40h - overtime income


def normal_gross(hours: float, hourly_rate: float) -> float:
    if hours <= 40:
        gross1 = hours * hourly_rate
        return gross1
    else:
        overtime = (hours - 40) * (hourly_rate * 1.5)
        gross2 = overtime + (40 * hourly_rate)
        return gross2


# overtime = 0
# def calculate_salary(gross_1: float, gross_2: float) -> float:
#     if float(gross_1.isdigit()) and hours <= 40:
#         return gross_1 == hours * hourly_rate

    # if float(gross_1) == hourly_rate * hours and hours <= 40:
    #     return gross_1
    # elif hours > 40:
    #     float(overtime) == hours - 40 and float(gross_2) == 40 * (hourly_rate) + overtime * (hourly_rate * 1.5)
    #     return gross_2


hourly_rate = float(input("What is your hourly rate?"))
hours = float(input("How many hours did you work this week?"))
print(normal_gross(hours, hourly_rate))


