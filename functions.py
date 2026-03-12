#1. Write a function to return the square of a number.

'''def square(num):
    return num * num

result = square(5)
print(result)'''

#2. Write a function to check whether a number is even or odd.

'''def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_even_odd(20))
print(check_even_odd(7))'''

# 3. Write a function to find the factorial of a number.

'''def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(factorial(7))'''

# 4. Write a function to find the sum of two numbers.

'''def sum_numbers(a, b):
    return a + b

result = sum_numbers(20, 250)
print(result)'''

# 5. Write a function to find the largest of two numbers.

'''def largest(a, b):
    if a > b:
        return a 
    else:
        return b

print(largest(10, 11))'''

# 6. Write a function to count vowels in a string.

'''def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Simun Gouda"))'''

# 7. Write a function to reverse a string.

'''def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello Simun"))'''

# 8. Write a function to check whether a number is positive, negative, or zero.

'''def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "nagative"
    else:
        return "zero"

print(check_number(2))
print(check_number(-2))
print(check_number(0))'''

# Write a function to check whether a number is positive, negative, or zero.
# A = \pi r^2

'''import math

def area_of_circle(radius):
    return math.pi * radius * radius

print(area_of_circle(2))'''

# 10. Write a function to find the average of numbers in a list.

'''def avg_number(num):
    total = sum(num)
    count = len(num)
    return total / count

num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(avg_number(num))'''

# 🔹 Intermediate Level (11–20)
# 11. Write a function to check whether a number is prime.

'''def is_prime(n):
    if n <=1:
        return "Not Prime"

    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

print(is_prime(7))
print(is_prime(0))
print(is_prime(1))
print(is_prime(8))'''

# 12. Write a function to find the largest number in a list.

'''def largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

nums = [10, 34, 54, 65, 67, 54]
print(largest_number(nums))'''

#13. Write a function to calculate the sum of digits of a number.

'''def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

print(sum_of_digits(2458712))'''

# 14. Write a function to reverse a number.

'''def reverse_number(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return reverse

print(reverse_number(1234))'''

# 15. Write a function to check whether a number is palindrome.

'''def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    
    if original == reverse:
        return "Palindrome"
    else:
        return "Not Plaindrome"

print(is_palindrome(151))
print(is_palindrome(152))'''

# 16. Write a function to generate Fibonacci series up to n terms.

'''def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(20)'''

# 17. Write a function to count words in a string.

'''def count_words(text):
    words = text.split()
    return len(words)

print(count_words("Simun is a good guy"))'''

# 18. Write a function to remove duplicates from a list.

'''def remove_duplicate(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

numbers = [12, 34, 56, 78, 90, 12, 23, 34, 56, 78]
print(remove_duplicate(numbers))'''

# 19. Write a function to find the minimum number in a list.

'''def find_minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum

nums = [45, 67, 34, 54, 67, 54]
print(find_minimum(nums))'''

# Write a function to check if a string is a palindrome.

'''def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome("radar"))
print(is_palindrome("Simun"))'''

#21. Write a function to find the second largest number in a list.

'''def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

nums = [10, 45, 23, 67, 12]
print(second_largest(nums))'''

#22. Write a function to merge two dictionaries.

'''def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

d1 = {"name1": "Simun", "age1": 23}
d2 = {"name2": "Rakesh", "age2": 29}

print(merge_dicts(d1, d2))'''

#23. Write a function to count frequency of characters in a string.

'''def char_frequency(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

print(char_frequency("hello"))
print(char_frequency("character"))'''

# Write a function to find common elements between two lists.

'''from mimetypes import common_types


def common_elements(list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common

a = [1, 2, 3, 4, 5]
b =  [3, 4, 5, 9, 7]

print(common_elements(a, b))'''

# 25. Write a function to check if two strings are anagrams.

'''def check_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return "Anagram"
    else:
        return "Not Anagram"

print(check_anagram("listen", "silent"))
print(check_anagram("hello", "world"))'''

# interview level questions
# Write a Python function to find the factorial of a number.

'''def find_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(find_factorial(5))'''

# 2. Write a function to check if a number is even or odd.

'''def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"

print(check_even_odd(2))
print(check_even_odd(3))'''

# 3. Write a function to calculate the square of a number.

'''from unittest import result

def square(num):
    return num**2

print(square(7))'''

# Write a function to calculate the cube of a number.

'''def cube(num):
    return num**3

print(cube(5))'''

# Write a function to find the sum of first n natural numbers.

'''def sum_natural(n):
    total = 0
    for i in range (1, n + 1):
        total = total + i

    return total

print(sum_natural(15))'''


# Write a function to find the sum of digits of a number.

'''def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    return total

print(sum_of_digits(1234567))'''

# Write a function to check whether a number is prime.

'''def is_prime(n):
    if n <=1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = 7

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")'''

# Write a function to generate Fibonacci series up to n terms.

'''def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(5)

def fibanacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibanacci(7)'''

# Write a function to check whether a number is palindrome.

from operator import truediv


def is_palindrome(n):
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
    print("Not a palindrome")



