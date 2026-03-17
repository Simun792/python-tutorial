"""
Encapsulation: Closing the access permission outside the of the class

    1. Appending double underscore (__) to a variable or function makes it unaccecible from ouside the class. But internal methods can access them.
    2. Appending single underscore (_) to a variable or function makes it accecible from ouside the class but it is a private varibale/method.
"""

class Person:
    def __init__(self, fname, lname, age, address) -> None:
        self.__fname = fname
        self.__lname = lname
        self._age = age
        self.__address = address

    def __get_full_name(self):
        return self.__fname + " " + self.__lname

    def get_person_details(self):
        details = f"Person Full Name: {self.__get_full_name()} \nPerson Age: {self._age}\nPerson Address: {self.__address}"
        return details


p = Person(fname="Sima", lname="Gouda", age=25, address="Golanda")
# print(p.__get_full_name())
print()
print(p.get_person_details())

print()
print(p._age)