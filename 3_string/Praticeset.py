'''1. Write a python program to display a user entered name followed by Good 
 Afternoon using input () function.''' 

# name = input("Enter your name: ")

# print(f"Good Afternoon {name} ")

# 2. Write a program to fill in a letter template given below with name and date. 
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> ''' 

print(letter.replace("<|Name|>", "Simun").replace("<|Date|>", "24 march 2025"))


# 3. Write a program to detect double space in a string. 
# 4. Replace the double space from problem 3 with single spaces. 


name = "Simun is a  good  boy"

print(name.replace("  ", " ")) 
print(name) # strings are immutable which means that you cannot change them by running functions on them

'''5. Write a program to format the following letter using escape sequence 
characters. 
letter = "Dear Harry, this python course is nice. Thanks!"'''

letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"

print(letter)

    


