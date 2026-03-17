from heapq import merge
from unicodedata import digit
from unittest import result


class person:
    def __init__(self, name, age) -> None:
        pass
        self.name = name
        self.age = age

p1 = person("Simun", 23)

# print(p1.name)
# print(p1.age)

#1. Write a program to print "Hello Python".

'''print("Hello World!")'''

#2. Write a program to take a number input and print it.

'''x = 5

print(x)'''

#3. Write a program to add two numbers.

'''a = 50
b = 40

print(a + b)'''

#4. Write a program to swap two numbers without using a third variable.

'''a = 5
b = 7

print(f"Before swap a = {a}, b = {b}")

a = a + b

b = a - b

a = a - b

print(f"After swap a = {a}, b = {b}")'''

#5. Write a program to check even or odd number.

'''num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")'''


#6. Write a program to find the largest of three numbers.

'''def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c 

print(largest_number(15, 28, 17))

a = 15
b = 18
c = 25

largest = max(a, b ,c)
print("Largest number:", largest)'''

#7. Write a program to calculate simple interest.

'''def simple_intrest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of intrest: "))
t = float(input("Enter Time: "))

result = simple_intrest(p, r, t)
print("Simple Intrest =", result)'''

#8. Write a program to calculate area of a circle.
import math

'''def area_of_circle(r):
    area = math.pi * r**2
    return area

radius = float(input("Enter radius: "))

result = area_of_circle(radius)
print("Area of circle= ", result)

def area_circle(r):
    return math.pi * r**2

r = float(input("Enter radius: "))

print("Area of circle =", area_circle(r))'''

#9. Write a program to convert Celsius to Fahrenheit.

'''def celsius_to_fahrenheit(c):
    return (c * 5/9) + 32

c = float(input("Enter Celsius: "))

print("Result =", celsius_to_fahrenheit(c))'''

'''def fahrenheit_to_celsius(f):
    return (f - 32) * (5/9)

f = float(input("Enter Fahrenhiet: "))

print("Result =", fahrenheit_to_celsius(f))'''

#10. Write a program to calculate factorial of a number.

'''def calculate_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact *i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", calculate_factorial(num))'''

#11. Write a program to print numbers from 1 to 100.

'''def print_numbers():
    for i in range(1 , 101):
        print(i)

print_numbers()'''

#12. Write a program to print sum of first n natural numbers.

'''def sum_of(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

num = int(input("Enter a number: "))
print("Result =", sum_of(num))'''

#13. Write a program to count digits in a number.

'''num = input("Enter a number: ")
print("Number of digits =", len(num))'''

'''def count_digits(n):
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))'''

#14 Write a program to reverse a number.

'''def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

num = int(input("Enter a number: "))
print("Reversed number =", reverse_number(num))

num = input("Enter a number: ")
print("Reversed number =", num[::-1])'''

#15. Write a program to check palindrome number.

'''def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome number")
else:
    print("Not palindrome number")

# using reverse string

num  = int(input("Enter a number :"))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")'''


#16 Write a program to find sum of digits of a number.

'''def sum_of(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10 
    return sum

num = int(input("Entera number: "))
print("Sum of digits =", sum_of(num))'''

#17 Write a program to check prime number.

'''def is_prime(n):
    if n <= 1:
        return "Not prime"
    
    for i in range(2, 0):
        if n % i == 0:
            return "Not prime"

    return "Prime"

num = int(input("Enter a number: "))
print(is_prime(num))'''

#18. Write a program to print Fibonacci series.

'''def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b

    
num = int(input("Enter number of terms: "))
fibonacci(num)'''


#20. Write a program to find largest number in a list.

numbers = [20, 30, 54, 32, 42, 43, 45, 32, 65, 23]
largest = max(numbers)

for num in numbers:
    if num > largest:
        largest = num

# print("Largest number is:", largest)

#21. Write a program to find smallest number in a list.

numbers = [20, 30, 54, 32, 42, 43, 45, 32, 65, 23]

smallest = min(numbers)

for num in numbers:
    if num < smallest:
        smallest = num

# print("Smallest number is:", smallest)

# Write a program to calculate average of numbers in a list.

'''def calculate_average(numbers):
    return sum(numbers) / len(numbers)

nums = [20, 30, 54, 32, 42, 43, 45, 32, 65, 23]
print("Average ia:", calculate_average(nums))

def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    return total / count   

nums = [20, 30, 54, 32, 42, 43, 45, 32, 65, 23]
print("Average ia:", calculate_average(nums))'''

#23. Write a program to remove duplicates from a list.

# a = [12, 32, 45, 12, 32, 67, 87, 54, 87, 12]

'''def remove_duplicates(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

numbers = list(map(int, input("Enter number: ").split()))

result = remove_duplicates(numbers)

print("List after removing duplicates: ", result)'''

# or

'''numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)'''

# 24. Write a program to merge two lists.

'''def merged_lists(a, b):
    return a + b

a = [10, 23, 45, 67, 89]
b = [11, 26, 25, 57, 39]

result = merged_lists(a, b)

print("Meerged list: ", result)'''

#25. Write a program to sort a list in ascending order.

def bubble_sort(numbers):
    # Get the total number of items in the list
    n = len(numbers)
    
    # Loop through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            
            # If the current number is bigger than the next number, swap them
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)

print("Sorted list using Bubble Sort:", sorted_list)
    










        
