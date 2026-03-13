"""
{
    "123": {
        "address": "Bengaluru",
        "name": "Rakesh"
    },


    "345": {
        "address": "Bhubaneswar",
        "name": "Sima"
    },

    "456": {
        "address": "Golanda",
        "name": "Raja"
    },
    
    "789": {
        "address": "Boripadar",
        "name": "Chandan"
    }
}
"""

from pprint import pprint

a = "Rakesh" # global variable

class Student:
    # class variable
    student_details = {

    }

    # class constructor. This will be executed on object creation
    def __init__(self) -> None:
        print("Constructor created !")

    # class function
    def add_student(self, roll_no, name, address):
        a = "sima" # local variable
        self.a = "Raja" # class variable
        if roll_no not in self.student_details.keys():
            self.student_details[roll_no] = {}
            self.student_details[roll_no]["name"] = name
            self.student_details[roll_no]["address"] = address

    def delete_student(self, roll_no):
        if roll_no in self.student_details.keys():
            del self.student_details[roll_no]

    def show_student_details(self, roll_no):
        if roll_no in self.student_details.keys():
            pprint(self.student_details[roll_no])
        else:
            pprint("No student found with this roll no: ", roll_no)

    def show_all_students(self):
        pprint(self.student_details)



st = Student() # Class obhect creation
st.add_student(
    roll_no=123, 
    name="Rakesh",
    address="Bengaluru"
)

st.add_student(
    roll_no=345, 
    name="Sima",
    address="Bhubaneswar"
)


st.add_student(
    roll_no=456, 
    name="Raja",
    address="Golanda"
)

st.add_student(
    roll_no=789, 
    name="Chandan",
    address="Boripadar"
)

pprint("Student before deletion***************")
st.show_all_students()
print()
print()
st.delete_student(roll_no=456)

pprint("Student after deletion***************")
st.show_all_students()
print()
print()

pprint("Student with roll no *********************")
st.show_student_details(roll_no=123)
