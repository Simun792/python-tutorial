'''1. Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up! 

words = {
    "madat": "help",
    "kursi": "chair",
    "billi": "cat"
}

word = input("Enter the word you want meaning of: ")

print(words[word]) '''

'''2. Write a program to input eight numbers from the user and display all the unique 
numbers (once). 

s = set()

n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)'''

#3. Can we have a set with 18 (int) and '18' (str) as a value in it? 

s = set()
s.add(18)
s.add("18")

print(s)