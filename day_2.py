""" Exercise 1: Basic Input & Response
Task:
Ask the user their name
Respond with a greeting"""
user_name = input("Enter your name:")
print(f"Hello, {user_name}")


"""Exercise 2: Simulate a Search Request
 Task:
Ask the user what they want to search
Respond like a browser"""
search_request = input("Enter your search request:")
print(f"{search_request} AlX is a tech program for the youth in Africa")


""" Exercise 3: Favorite Food App
 Task:
Ask user their favorite food
Respond with a sentence"""
favourite_food = input("What is your favourite food?:")
print(f"My favourite food is {favourite_food}.")


"""Exercise 4: Simple Login (Important)
 Task:
Ask for username and password
Check if correct"""
user_name = input("Enter the user name:")
password = int(input("Enter the password:"))
if user_name == "Caroline" and password == 1234:
    print("Access granted")
else:
    print("Access denied")


"""Exercise 5: Age Checker
 Task:
Ask user age
Check if adult"""
age = int(input("Enter your age:"))
if age == 18:
    print("User is an adult.")
else:
    print("User is a child")