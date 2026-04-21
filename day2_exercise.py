"""1. Greeting App
Ask the user their name and print:
“Welcome, NAME"""
name = input("Enter your name:")
print(f"Welcome, {name}")


"""2. Year of Birth Calculator
Ask age, then print:
“You were born in YEAR”
(Assume current year is 2026)"""
age = int(input("Enter your age:"))
current_year = 2026
year_of_birth = current_year - age
print(f"You were born in Year {year_of_birth}")


"""3. Simple Calculator (Addition)
Ask for two numbers and print their sum."""
first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
total = first_number + second_number
print(f"The sum of the two numbers is {total}")


"""4. Even or Odd Checker
Ask for a number and check:
even → “Even number”
odd → “Odd number”"""
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


"""5. Temperature Message
Ask temperature:
if above 30 → “It’s hot”
else → “It’s cold”"""
temperature = int(input("Enter the temperature:"))
if temperature > 30:
    print("It's hot")
else:
    print("It's cold")


"""6. Username Length
Ask for username and print:
“Your username has X characters”"""
user_name = input("Enter your user name:")
print(f"Your username has {len(user_name)} characters")


"""7. Password Check (Basic)
Ask password:
if password is “1234” → “Access granted”
else → “Access denied”"""
password = input("Enter the password:")
if password == "1234":
    print("Access granted")
else:
    print("Access Denied")


"""8. Simple Discount Checker
Ask for price:
if above 1000 → “You get a discount”
else → “No discount”"""
price = int(input("Enter the price:"))
if price > 1000:
    print("You get a discount")
else:
    print("No discount")


"""9. Age Category
Ask age:
below 13 → “Child”
13–17 → “Teen”
18+ → “Adult”"""
age = int(input("Enter the age:"))
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")


"""10. Mini Profile
Ask:
name
age
favorite food
Print in one sentence:
“My name is __, I am __ years old and I love __.”"""
name = input("Enter your name:")
age = int(input("Enter your age:"))
favorite_food = input("Enter your favorite food:")
print(f"My name is {name}, I am {age} years old and I love {favorite_food}")
