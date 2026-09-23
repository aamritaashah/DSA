#1. write a function to print "hello 'world!",

def hello():
    print("Hello, World!")
    hello()

#2. write a function that takes a name and print a greeting.

def greeting(name):
    print(f"Hello,{name}!")
    greeting("amrita")

#3.write a function to add a two numbers.

def add_number(a,b):
    return a+b
res=add_number(2,20)
print(f"Addition result:{res}")

#4. write a function to find the square of a number.

def square_number(num):
    return num**2
res=square_number(8)
print(f"square result:{res}")

#5. write function to check whether a number is even or odd.

def odd_even(num):
    return "Even" if num %2==0 else "Odd"
result =odd_even(8)
print(f"the Number Is:{result}")

