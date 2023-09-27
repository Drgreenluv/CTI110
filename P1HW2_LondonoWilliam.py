#P1HW2_LondonoWilliam.py
# A brief description of the project

# 09/26/2023

# CTI-110 P1HW2 - Travel Expense

# William Londono

#
budget = int(input("Enter budget: "))
destination = input("Enter your travel destination: ")
fuel_cost = int(input("How much will you spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

print("----------Travel Expenses----------")
print("Location:",destination)
print("Initial Budget:",budget)
print("\n") 
print("Fuel:", fuel_cost)
print("Accomodation:", accommodation)
print("Food:", food)
print("\n")
print("Remaining Balance:", budget-fuel_cost-accommodation-food)
