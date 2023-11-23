# CTI-110
# P4HW2 - Salary Calculator
# William Londono
# 23NOV2023
#

"""
Pseudocode:
1. Initialize constants for OVERTIME_MULTIPLIER and MAX_REGULAR_HOURS.
2. Initialize total counters for overtime pay, regular pay, and gross pay.
3. Initialize a counter for the number of employees.

Function calculate_pay(hours, rate):
    1. Check if hours are greater than MAX_REGULAR_HOURS to calculate overtime.
    2. If so, calculate overtime pay and regular pay separately.
    3. If not, all hours are regular, and no overtime pay is calculated.
    4. Calculate gross pay by adding regular pay and overtime pay.
    5. Return the calculated regular pay, overtime pay, and gross pay.

Main Program:
1. Loop over a predefined list of employees with their names, hours worked, and pay rates.
    1. For each employee, call calculate_pay with their hours and pay rate.
    2. Add the returned pay amounts to the total counters.
    3. Increase the employee counter.
    4. Print out the pay details for the employee.
2. After all employees are processed, print out the total amounts and number of employees.
"""
# Constants for the calculations
OVERTIME_MULTIPLIER = 1.5
MAX_REGULAR_HOURS = 40

# Initialize totals and counters
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
num_employees = 0

# Function to calculate pay
def calculate_pay(hours, rate):
    if hours > MAX_REGULAR_HOURS:
        overtime_hours = hours - MAX_REGULAR_HOURS
        overtime_pay = overtime_hours * rate * OVERTIME_MULTIPLIER
        regular_pay = MAX_REGULAR_HOURS * rate
    else:
        overtime_pay = 0.0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, gross_pay

# Predefined employee data
employees = [
    {"name": "John Doe", "hours_worked": 38, "pay_rate": 25},
    {"name": "Jane Smith", "hours_worked": 42, "pay_rate": 30},
    {"name": "Emily Davis", "hours_worked": 45, "pay_rate": 20},
    {"name": "Michael Brown", "hours_worked": 33, "pay_rate": 22},
    {"name": "Jessica Taylor", "hours_worked": 50, "pay_rate": 15}
]

# Main program
while True:
    # Simulated user input for employee data
    for employee in employees:
        employee_name = employee["name"]
        pay_rate = employee["pay_rate"]
        hours_worked = employee["hours_worked"]

        regular_pay, overtime_pay, gross_pay = calculate_pay(hours_worked, pay_rate)

        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        num_employees += 1

        print(f"Employee Name: {employee_name}")
        print(f"Hours Worked: {hours_worked:.2f}")
        print(f"Overtime Pay: ${overtime_pay:.2f}")
        print(f"Regular Pay: ${regular_pay:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print("-" * 40)

    break  # Break the loop since we are not taking actual user input

print(f"Total number of employees: {num_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

