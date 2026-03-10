'''4. What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

print(len(s))

5. s = {} 
    What is the type of 's'? 

s = {}
print(type(s))'''

'''6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. 

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d) '''

'''7. If the names of 2 friends are same; what will happen to the program in problem 
6? '''

'''9. Can you change the values inside a list which is contained in set S? '''

s = {8, 7, 12, "Harry", [1,2]}