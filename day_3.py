"""1. Even AND Divisible by 3
Ask number:
if divisible by 2 AND 3 → print message
else → print another message"""
number = int(input("Enter a number:"))
if number % 2 == 0 and number % 3 == 0:
    print("Number is divisible by both 2 and 3")
else:
    print("Number is NOT divisible by both 2 and 3")


"""2. Password Length Checker
Ask password:
if length ≥ 8 → Strong
else → Weak"""
password = input("Enter a password:")
if len(password) >= 8:
    print("Strong")
else:
    print("Weak")


"""3. Grade System
Ask marks:
80+ → A
70–79 → B
60–69 → C
below → D"""
marks = int(input("Enter the marks:"))
if marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


"""4. ATM Withdrawal
Ask:
balance
withdrawal
Check:
if withdrawal ≤ balance → success
else → insufficient funds"""
balance = int(input("Enter the balance:"))
withdrawal = int(input("Enter the withdrawal:"))
if withdrawal <= balance:
    print("Transaction successful")
else:
    print("insufficient funds")


"""5. Login with 2 Conditions
Ask:
username
password
Check:
both must be correct"""
username = input("Enter the username:")
password = input("Enter the password:")
if username == "Caroline" and password == "Yellow":
    print("Login successful")
else:
    print("Invalid username or password")

