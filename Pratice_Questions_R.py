'''1. Write a Python program to store your name, age, and height and print them.
name = input("Enter your name: ")
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

# from unittest import result


# a = "100"
# # num = int(a)
# # result = num + 50

# # print(result)

# print(int(a) + 50)

#5. Write a program to check whether a number is greater than 100 (boolean result).

# a = (99 > 100)
# print(a)

# num = int(input("Enter a number: "))
# result = num > 100

# print(result)

#6. Write a program to concatenate two strings.

# a = str(input("Enter your first_name: "))
# b = str(input("Enter your last_name: "))

# print(a + " " + b)

#7. Write a program to find the length of a string.

# a = ("Simun Gouda")

# print(len(a))

# a = input("Enter a string: ")

# print("Lenth of the string is:", len(a))

#8. Convert a float number to integer.

# a = 5.0

# print(int(a))

# a = float(input("Enter a float number: "))

# print(int(a))

#9. Write a program to check if a number is even or odd.

# a = int(input("Enter a number: "))

# if a % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# temp = a
# a = b 
# b = temp

# print("After swapping: ")
# print("a =", a)
# print("b =", b)

#11. Create a list of 5 numbers and print it.
# 2. Add a new element to the list.
# 3. Remove an element from the list.

# print(a)
# for i in a:
#     print(i)

# a.append(98)
# print(a)

# a.remove(12)
# print(a)

# Print the largest number in a list.

# a = [12, 34, 56, 65, 45]

# largest = a[0]

# for i in a:
#     if i > largest:
#         largest = i

# print("Largest number:", largest)

#15. Print the sum of all elements in a list.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))
# e = int(input("Enter a number: "))

# numbers = [a, b, c, d, e]

# print("Sum = ", sum(numbers))

# a = [12, 34, 56, 65, 45]

# print(sum(a))

# 16.Reverse a list.

# a = [12, 34, 56, 65, 45]

# a.reverse
# print(a)

# Find the index of an element in a list.

# a = [12, 34, 56, 65, 45]

# print(a.index(56))

# Sort a list in ascending order.

# a = [98, 88, 79, 86, 65, 97, 93, 99]

# a.sort()
# print(a)

# #19. Count how many times an element appears in a list.

# a = [45, 48, 35, 25, 36, 46, 25, 36, 35, 48, 49, 45]

# print(a.count(48))

#20. Merge two lists.

# a = [45, 38, 48, 32]

# b = [96, 92, 93, 95, 86, 65]

# sorted_merge = sorted (a + b)

# print(sorted_merge)
