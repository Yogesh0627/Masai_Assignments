class Student:
    def __init__(self,name,rollno,age):
        self.name = name # Public Access Specifiers
        self._rollno = rollno # Protected  Access Specifiers
        self.__age = age # Private Access Specifiers
    def __display(self):
        print(f" Hello myself {self.name} {self.age} years old with {self._rollno} Rollno and i am from Student Class")

class Branch(Student):
    def show(self):
        print(f'My rollno is {self.rollno_}')
# s1 = Student('Yogesh')
# s1.display()

b1= Branch('Deepak',21)