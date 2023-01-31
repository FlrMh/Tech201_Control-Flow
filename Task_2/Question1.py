# User worked hours task

# Ask for hours worked and rate of pay;
# Calculate gross pay for the week;
# Note: Pay over 40h is 1.5 x hour rate.

print("Welcome to your income calculator!")

hourly_rate = float(input("Please provide your hourly rate."))


worked_hours = float(input("Please provide the amount of hours worked this week."))
if worked_hours > 40:
    overtime = worked_hours - 40
    overtime_pay = overtime * (hourly_rate * 1.5)
    gross_income = 40 * hourly_rate + overtime_pay
else:
    gross_income = worked_hours * hourly_rate

print(f"Your gross income for this week, when you worked {worked_hours}, will be {gross_income}.")



