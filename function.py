# FUNCTIONS WITH PRINT



# 1. Print "Hello, World!"
def hello():
    print("Hello, World!")

hello()


# 2. Take a name and print a greeting
def greet(name):
    print("Hello", name)

greet("Rahul")


# 3. Add two numbers
def add(a, b):
    return a + b

print("Addition:", add(10, 20))


# 4. Find the square of a number
def square(n):
    return n * n

print("Square:", square(5))


# 5. Check whether a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", even_odd(10))


# 6. Find the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", maximum(10, 20))


# 7. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print("Fahrenheit:", celsius_to_fahrenheit(25))


# 8. Calculate the area of a circle
def circle_area(radius):
    return 3.14 * radius * radius

print("Area of Circle:", circle_area(5))


# 9. Calculate factorial of a number
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print("Factorial:", factorial(5))


# 10. Check positive, negative or zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print("Number is:", check_number(-5))


# 11. Find maximum of three numbers
def maximum_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Maximum of three:", maximum_three(10, 25, 15))


# 12. Count vowels in a string
def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiouAEIOU":
            count += 1

    return count

print("Number of vowels:", count_vowels("Hello World"))


# 13. Reverse a string
def reverse_string(text):
    return text[::-1]

print("Reversed string:", reverse_string("Python"))


# 14. Check whether a string is palindrome
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print("Palindrome:", palindrome("madam"))


# 15. Find sum of all elements in a list
def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print("Sum of list:", list_sum([10, 20, 30, 40]))


# 16. Find largest element in a list
def largest(numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

print("Largest element:", largest([10, 50, 20, 40]))


# 17. Remove duplicate elements from a list
def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# 18. Count how many times an element appears
def count_element(numbers, target):
    count = 0

    for num in numbers:
        if num == target:
            count += 1

    return count

print("Count of 2:", count_element([1, 2, 2, 3, 2, 4], 2))


# 19. Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("Is Prime:", is_prime(7))


# 20. Return all prime numbers between two numbers
def prime_numbers(start, end):
    primes = []

    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)

    return primes

print("Prime numbers:", prime_numbers(10, 30))


# 21. Calculate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print("Fibonacci:", fibonacci(10))


# 22. Find second-largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]

print("Second largest:", second_largest([10, 50, 20, 40, 30]))


# 23. Sort a list without using sort()
def my_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

print("Sorted list:", my_sort([5, 2, 8, 1, 3]))


# 24. Merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for num in list1:
        if num not in result:
            result.append(num)

    for num in list2:
        if num not in result:
            result.append(num)

    return result

print("Merged list:", merge_lists([1, 2, 3, 4], [3, 4, 5, 6]))

