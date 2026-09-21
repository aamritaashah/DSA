# 4. Conditions

# 1. Check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Check whether a person is eligible to vote.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 3. Find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# 4. Check whether a year is a leap year.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year.")
elif year % 100 == 0:
    print("It is not a leap year.")
elif year % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")
    

# 5. Create a grade system based on marks.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")

# 6. Check whether a number is divisible by 5 and 11.


num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")
    

# 7. Create a simple calculator using if-elif-else.

# Simple calculator using if-elif-else

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")


