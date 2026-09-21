
# 3.Operators

# 1. Perform addition, subtraction, multiplication, and division.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2. Find the remainder and quotient of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Quotient:", quotient)
print("Remainder:", remainder)

# 3. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 4. Compare two numbers using relational operators.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 5. Demonstrate logical operators (and, or, not).

a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)

# 6. Demonstrate assignment operators (+=, -=, *=, /=).

x = 10

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 4
print("After /= :", x)

# 7. Find the largest of two numbers using comparison operators.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number:", a)
elif b > a:
    print("Largest number:", b)
else:
    print("Both numbers are equal.")
    

