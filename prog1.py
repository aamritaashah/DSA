#1. variables

#1.create varibles to store name, age and city and display them.

name = "John"
age = 20
city = "Rajkot"

print("Name:", name)
print("Age:", age)
print("City:", city)


#2. swap the value of two variables.

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)



#3. Calculate the area of a rectangle using variables.
length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"\nThe area of the rectangle is: {area}")



# 4. Calculate simple interest using variables.

principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the years: "))

simple_interest = (principal * rate * time) / 100

print(f"\n--- Results ---")
print(f"Principal: {principal:,.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time: {time} years")
print(f"Total Simple Interest Earned: {simple_interest:,.2f}")


# 5. Convert Celsius temperature to Fahrenheit.
celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print("\ncelsius: ",celsius)
print("fahrenheit: ",fahrenheit)





