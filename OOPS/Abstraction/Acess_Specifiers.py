'''
Public Specifiers are those whose can acess Publicaly

Private Specifers can use with in the class only although we can
access private specifiers with the help of name mangling / creating
public display method in class / Getter and setter

protected specifiers are those whose can access only
in class and derived class
'''


class Student:
    def __init__(self,name,rollno,age):
        self.name = name # Public Access Specifiers
        self._rollno = rollno # Protected  Access Specifiers
        self.__age = age # Private Access Specifiers
    def display(self):
        print(f" Hello myself {self.name} and i am from Student Class")

class Branch(Student):
    def show(self):
        print(f'My rollno is {self.rollno_}')
# s1 = Student('Yogesh')
# s1.display()

b1= Branch('Deepak',21)