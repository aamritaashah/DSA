#2.Data types

#1.Demonstrate int, float, str, bool, and complex.

age = 20              # int
height = 5.8          # float
name = "John"         # str
is_student = True     # bool
number = 3 + 4j       # complex

print("Integer:", age)
print("Float:", height)
print("String:", name)
print("Boolean:", is_student)
print("Complex:", number)


# 2. Accept two numbers and display their data types.

'''num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("First number:", num1)
print("Data type:", type(num1))

print("Second number:", num2)
print("Data type:", type(num2))'''


# 3. Convert a string number into an integer and float.

num = "25"

integer_num = int(num)
float_num = float(num)

print("String:", num)
print("Integer:", integer_num)
print("Float:", float_num)

# 4.Find the length of a string.

text = "Hello World"

length = len(text)

print("String:", text)
print("Length:", length)

# 5.Create a list, tuple, set, and dictionary and display their types.

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dictionary = {"name": "John", "age": 20}

# Display their values and types
print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dictionary)
print("Type:", type(my_dictionary))
