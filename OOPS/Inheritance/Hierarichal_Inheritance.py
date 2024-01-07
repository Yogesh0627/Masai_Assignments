'''
Mulitple Child classes can create from single parent
'''

# class Human:        # ===> Parent Class (Grand-Parent)
#     def __init__(self,heart):
#         print(f'Human init Called')
#         self.heart=heart
#         self.num_nose = 1
#         self.num_ear = 2
#         self.num_eye = 2
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')


# class Male (Human):            # ===> Child Class
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#
#     # Sibling  Class
#
# class Female (Human):
#     pass

'''
Practice Problem

Create One SuperClass {Person} having 2 attributes 2 Methods 2 classes are derived from Person Class
Faculty Class and student class with one attributes and one method of their own tried to access the 
person class attributes with the help objects of student and faculty
'''

class Person:
    def __init__(self,name ,contact,address):
        self.name = name
        self.contact = contact
        self.address = address

    def read(self):
        print('I can Read')
    def write(self):
        print('I Can Write')


class Student(Person):
    def __init__(self,name,contact,address,rollno):
        Person.__init__(self,name,contact,address)
        # super.__init__(self,name,contact,address)
        self.RollNo = rollno
    def showDetails(self):
        print(f" I am {self.name} and my rollno is {self.RollNo}")

class Faculty(Person):
    def __init__(self,name,contact,address,subject):
        super().__init__(name,contact,address)
        self.subjectToTeach = subject

deepak = Student('Deepak',9041996384,'Fazilka Punjab',4)
# print(deepak.RollNo)
deepak.showDetails()


heera = Faculty('Heera',9876543210,'Sagar MP','DSA')
print(heera.name)