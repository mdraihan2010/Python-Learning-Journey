# Write a Program to input an employee's name, basic salary, and bonus. Calculate the total salary, average monthly salary (assuming the total is for 12 months), and check whether the total salary is greater than or equal to 50000.

name = input("Enter employee's name: ")
basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))

total_salary = basic_salary + bonus
average_monthly_salary = total_salary / 12
is_high_earner = total_salary >= 50000

print("Employee Name:", name)
print("Total Salary:", int(total_salary))
print("Average Monthly Salary:", round(average_monthly_salary, 2))
print("Is High Earner:", is_high_earner)