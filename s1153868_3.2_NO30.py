#NO30 Overtime pay
hourly_wage=float(input("Enter hourly wage: "))
hours_worked=float(input("Enter number of hours worked: "))
if hours_worked <= 40:
    print("Total pay is $", hourly_wage*hours_worked)
else:
    regular_pay = hourly_wage * 40
    overtime_pay = hourly_wage * 1.5 * (hours_worked - 40)
    print("Gross pay for week is $", regular_pay + overtime_pay)
    