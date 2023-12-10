# Math Quiz Program
# Date: 05DEC2023
# CTI-110 P5HW2 - Math Quiz
# William Londono

import random

def main():
    while True:
        print("\nWelcome to Math Quiz")
        print("\nMAIN MENU")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        
        choice = input("Please choose one of the menu options: ")
        
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...")
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2
    print(f"\n{num1} + {num2}")
    quiz_user(correct_answer)

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    print(f"\n{num1} - {num2}")
    quiz_user(correct_answer)

def quiz_user(correct_answer):
    guess_count = 0
    while True:
        user_answer = int(input("Enter answer: "))
        guess_count += 1
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

# Start the program
if __name__ == "__main__":
    main()
