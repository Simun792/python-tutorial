# 1. Write a Python program to store your name, age, and height and print them.
'''name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your hright: "))

print("Name:", name)
print("Age:", age)
print("Height", height)'''

#2. Write a program to add two integers entered by the user.

'''a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

sum = a + b

print("Sum =", sum)'''

#3. Write a program to multiply a float and an integer.

'''from operator import mul


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

mul = a * b 

print("Mul: " , mul)'''

# Convert a string "100" to integer and add 50 to it.

'''from unittest import result


a = "100"
# num = int(a)
# result = num + 50

# print(result)

print(int(a) + 50)'''

#5. Write a program to check whether a number is greater than 100 (boolean result).

'''a = (99 > 100)
print(a)

num = int(input("Enter a number: "))
result = num > 100

print(result)'''

#6. Write a program to concatenate two strings.

'''a = str(input("Enter your first_name: "))
b = str(input("Enter your last_name: "))

print(a + " " + b)'''

#7. Write a program to find the length of a string.

'''a = ("Simun Gouda")

print(len(a))

a = input("Enter a string: ")

print("Lenth of the string is:", len(a))'''

#8. Convert a float number to integer.

'''a = 5.0

print(int(a))

a = float(input("Enter a float number: "))

print(int(a))'''

#9. Write a program to check if a number is even or odd.

'''a = int(input("Enter a number: "))

if a % 2 == 0:
    print("Even number")
else:
    print("Odd number")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b 
b = temp

print("After swapping: ")
print("a =", a)
print("b =", b)'''

#11. Create a list of 5 numbers and print it.
# 2. Add a new element to the list.
# 3. Remove an element from the list.

'''print(a)
for i in a:
    print(i)

a.append(98)
print(a)

a.remove(12)
print(a)'''

# Print the largest number in a list.

'''a = [12, 34, 56, 65, 45]

largest = a[0]

for i in a:
    if i > largest:
        largest = i

print("Largest number:", largest)'''

#15. Print the sum of all elements in a list.

'''a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))

numbers = [a, b, c, d, e]

print("Sum = ", sum(numbers))

a = [12, 34, 56, 65, 45]

print(sum(a))'''

# 16.Reverse a list.

'''a = [12, 34, 56, 65, 45]

a.reverse
print(a)'''

# Find the index of an element in a list.

'''a = [12, 34, 56, 65, 45]

print(a.index(56))

Sort a list in ascending order.

a = [98, 88, 79, 86, 65, 97, 93, 99]

a.sort()
print(a)'''

# #19. Count how many times an element appears in a list.

'''a = [45, 48, 35, 25, 36, 46, 25, 36, 35, 48, 49, 45]

print(a.count(48))'''

#20. Merge two lists.

'''a = [45, 38, 48, 32]

b = [96, 92, 93, 95, 86, 65]

sorted_merge = sorted (a + b)

print(sorted_merge)'''

#21. Create a tuple with 5 elements.
# Access the third element of a tuple.

'''a = (12, 34, 65, 67, 89, "Simun", "Rakesh")

last_element = a[-1]

print(last_element)'''

#23. Count occurrences of an element in a tuple.

'''a = (12, 34, 65, 67, 89, 65, "Simun", "Rakesh")

print(a.count(65))'''

# #24 Find the length of a tuple.

'''a = (12, 34, 65, 67, 89, 65, "Simun", "Rakesh")

print(len(a))'''

# # 25. Convert a **tuple into a list**.

'''a = (12, 34, 65, 67, 89, 65, "Simun", "Rakesh")

print(list(a))'''

# 26.Create a dictionary with name, age, city.

'''a = {"name": "Simun", "age": 20, "city": "Golanda"}

print(a)'''

# # 27. Add a new key-value pair to the dictionary.

# a["email"] = "simun@gmail.com"

# print(a)

# # # 28. Remove a key-value pair from the dictionary.

# # a.pop("age")
# # print(a)

# #29. Print only the keys of the dictionary.

# a = {"name": "Simun", "age": 20, "city": "Golanda"}

# print(a.keys())

# #30. Print only the values of the dictionary.

# a = {"name": "Simun", "age": 20, "city": "Golanda"}

# print(a.values())

# # #31. Print the key-value pairs of the dictionary.

# # a = {"name": "Simun", "age": 20, "city": "Golanda"}

# # print(a.items())

# # #32. Update the value of a key in the dictionary.

# # a = {"name": "Simun", "age": 20, "city": "Golanda"}

# # a["age"] = 21

# # print(a)

# # #33. Remove a key-value pair from the dictionary.
# # a.pop("age")
# # # print(a)

# # #34. Add a new key-value pair.

# # a = {"name": "Simun", "age": 20, "city": "Golanda"}

# # a["email"] = "simun@gmail.com"
# # print(a)

# # #35. Get the value of a key from the dictionary.

# # print(a["email"])

# # #36. Check if a key exists in the dictionary.

# # print("email" in a)

# # 37. Loop through a dictionary and print key and value.

# # a = {"name": "Simun", "age": 20, "city": "Golanda"}

# # # for key, value in a.items():
# # #     print(key, value)


# # # # Update the value of an existing key.

# # # a = {"name": "Simun", "age": 20, "city": "Golanda"}
# # # a["age"] = 21
# # # print(a)

# # # Merge two dictionaries.

# # a = {"name": "Simun", "age": 20, "city": "Golanda"}
# # b = {"email": "simun@gmail.com"}
# # c = a | b
# # print(c)


# # # Count number of items in dictionary.

# # print(len(a))

# # 38. Create a set with 5 elements.

# # a = {12, 34, 56, 65, 45}
# # print(a)

# # # # 39. Add an element to a set.

# # a.add(78)
# # print(a)

# # # 40. Remove an element from a set.

# # a.remove(12)
# # print(a)

# # # 41. Find the union of two sets.

# # a = {12, 34, 56, 65, 45}
# # b = {96, 92, 93, 95, 86, 65}
# # print(a.union(b))

# # # 42. Find the intersection of two sets.

# # a = {12, 34, 56, 65, 45}
# # b = {96, 92, 93, 95, 86, 65}
# # print(a.intersection(b))

# # # 43. Find the difference of two sets.  

# # a = {12, 34, 56, 65, 45}
# # b = {96, 92, 93, 95, 86, 65}
# # print(a.difference(b))

# # 44. Check if a set is a subset of another set.

# a = {12, 34, 56, 65, 45}
# b = {96, 92, 93, 95, 86, 65}
# print(a.issubset(b))

# # 45. Check if a set is a superset of another set.  

# a = {12, 34, 56, 65, 45}
# b = {96, 92, 93, 95, 86, 65}
# print(a.issuperset(b))

# # 46. Check if a set is a proper subset of another set.

# a = {12, 34, 56, 65, 45}
# b = {96, 92, 93, 95, 86, 65}
# print(a.issuperset(b))

# # 47. Check if a set is a proper superset of another set.

# a = {12, 34, 56, 65, 45}
# b = {96, 92, 93, 95, 86, 65}
# print(a.issuperset(b))

# Check if an element exists in a set.

# a = {12, 34, 56, 65, 45}
# print(65 in a)

#51.Print numbers 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i)
#     break

# 52. Print the sum of first n natural numbers using a for loop.

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# Print even numbers between 1–20.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# Print the multiplication table of a number.

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# Calculate the sum of numbers from 1 to 100.

# sum = 0
# for i in range(1, 101):
#     sum += i # sum = sum + i
# print(sum)

# Print each character of a string.

# a = "Simun"
# for i in a:
#     print(i)

# # Print elements of a list using loop.

# a = [12, 34, 56, 65, 45]
# for i in a:
#     print(i)

# Print elements of a tuple using loop.

# a = (12, 34, 56, 65, 45)
# for i in a:
#     print(i)

# Print elements of a dictionary using loop.

# a = {"name": "Simun", "age": 20, "city": "Golanda"}
# for key, value in a.items():
#     print(key, value)

# # Print elements of a set using loop.

# a = {12, 34, 56, 65, 45}
# for i in a:
#     print(i)


# Print numbers 1–10 but stop when number = 5.

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
#     continue

# Print numbers 1–10 but skip number 5.

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
    
# Print numbers 1–20 but skip multiples of 3.

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)
    

# Stop a loop when a negative number is found in a list.

# a = [12, 34, 56, 65, 45, -12, 34, 56, 65, 45]
# for i in a:
#     if i < 0:
#         break
#     print(i)

#     # to skip nagative number?
    
#     a = [12, 34, 56, 65, 45, -12, 34, 56, 65, 45]
# for i in a:
#     if i < 0:
#         continue
#     print(i)
    

# Check if a number is between 10 and 50.

# num = int(input("Enter a number: "))
# if num > 10 and num < 50:
#     print("Number is between 10 and 50")
# else:
#     print("Number is not between 10 and 50")


# Check if a person is eligible to vote (age ≥ 18).

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# Check if a number is positive or negative.

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# Check if a number is divisible by 3 OR 5.

# num = int(input("Enter a number: "))
# if num % 3 == 0 or num % 5 == 0:
#     print("Number is divisible by 3 or 5")
# else:
#     print("Number is not divisible by 3 or 5")


# # Check if a number is divisible by 3 and 5.

# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Number is divisible by 3 and 5")
# else:
#     print("Number is not divisible by 3 and 5")

# Write a program to find the largest of three numbers.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if a > b and a > c:
#     print("A is the largest number")
# elif b > a and b > c:
#     print("B is the largest number")
# else:
#     print("C is the largest number")

# Print numbers 1 to 10 using while loop.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Print the sum of numbers from 1 to n.

# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# Print multiplication table using while loop.

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1

# Reverse a number using while loop.

# n = int(input("Enter a number: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)

# Keep asking user for password until correct.

# password = "12345"
# while True:
#     guess = input("Enter the password: ")
#     if guess == password:
#         print("Password is correct")
#         break
#     else:
#         print("Password is incorrect")

# Write a function to add two numbers.

# def add_numbers(a, b):
#     return a + b

# print(add_numbers(10, 20))

# Write a function to find factorial of a number.

# from unittest import result


# def factorial(n):
#     fact = 1 
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# num = int(input("Enter a number: "))
# result = factorial(num)
# print("Factorial is:", result)

# Write a function to check prime number.

# def check_prime(n):
#     if n <= 1:
#         return "Not Prime"

#     for i in range(2, n):
#         if n % i == 0:
#             return "Not Prime"

#     return "Prime"

# num = int(input("Enter a number: "))
# print(check_prime(num))

# Write a function to reverse a string.

# def reverse_string(text):
#     return text[::-1]

# word = input("Enter a string: ")
# print("Reversed string:", reverse_string(word))

# Write a function to find largest number in a list.

'''def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

nums = [12, 45, 7, 89, 34]
print("Largest number is: ", find_largest(nums))'''

# Write a function to count vowels in a string.

'''def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

word = input("Enter a string: ")
print("Number of vowels:", count_vowels(word))

# better verison'''

'''def count_vowels(text):
    return sum(1 for char in text if char.lower() in "aeiou")

word = input("Enter a string: ")
print("Number of vowels:", count_vowels(word))'''

# Write a function that returns square of a number.

'''def squre(n):
    return n**2

num = int(input("Enter a number: "))
print("Squre is:", squre(num))'''
# Write a function to check palindrome string.

'''def check_Palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


word = input("Enter a string:")
print(check_Palindrome(word))'''

# Create a file and write "Hello Python".

'''file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()'''

'''with open("hello.txt", "w") as file:
    file.write("Hello Simun")'''

# Read the content of a file.

'''with open("Hello.txt", "r") as file:
    content = file.read()
    print(content)'''

# Append new text to an existing file.

'''with open("hello.txt", "a") as file:
    file.write("\nWelcome to Python")'''

# Count number of lines in a file.

'''with open("hello.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))'''

'''from sqlite3 import connect


count = 0
with open("hello.txt", "r") as file:
    for line in file:
        count += 1

print(count)'''

# Count number of words in a file.

'''with open("hello.txt", "r") as file:
    connect = file.read()
    words = connect.split()
    print(len(words))'''

# Read a file and print only lines containing the word "Python".

'''with open("hello.txt", "r") as file:
    for line in file:
        if "python" in line:
            print(line)'''

# Copy contents of one file to another.

'''with open("source.txt", "r") as source:
    with open("destination.txt", "w") as dest:
        content = source.read()
        dest.write(content)'''

# Write a list of numbers into a file.

'''numbers = [10, 20, 30, 40, 50]

with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")'''


# Read numbers from a file and calculate sum.

'''total = 0 

with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line)
        total += num

print("sum", total)'''

# Create a program that stores student names in a file.

'''with open("student.txt", "w") as file:
    for i in range(3):
        name = input("Enter student name: ")
        file.write(name + "\n")'''