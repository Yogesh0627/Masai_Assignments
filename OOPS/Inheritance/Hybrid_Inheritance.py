'''
Combiniation of more than one inheritance
'''

# class A:
#     def display(self):
#         print('Display of A')
#
# class B(A):
#     def display(self):
#         super().display()
#         # print('Display from B')
#
# class C:
#     def show(self):
#         print('Hii from c Class')
#
# class D(B,C):
#     def printing(self):
#         print ('namaste from D')
#     def AccessDispalyFromA(self):
#         super().display()
#
# d1 = D() # homwork Acess Display from A in D
# # d1.display()
# d1.AccessDispalyFromA()

'''
Practice Problem 

Write a Program for hybrid Inheritance take a Parent Class
{University} and a attribute and method {showDetails}
from university make two child classes one course and other is branch
with a one Attribute and one method showDetails
theres a one more  class Student with a attribute and 
one method showdetials student class is 
child class of course and branch, there is another 
Class Faculty which is child of Branch class

make showdetails function common in university class and use it with
inherit way

'''

# class University:
#     def __init__(self,universityName):
#         self.UniversityName = universityName
#
#     def showDetails(self,UniversityName):
#         print(f'Details are as follow {UniversityName}')
#
# class Course(University):
#     def __init__(self,courseName):
#         self.course = courseName
#     def printde(self):
#         super().showDetails(self.course)
#         # University.showDetails(self,self.course)
#
# class Branch(University):
#     def __init__(self,branchName):
#         self.branch = branchName
#     def printBranch(self):
#         # University.showDetails(self,self.branch)
#         super().showDetails(self.branch)
# class Student(Course,Branch):
#     def __init__(self,name):
#         self.name = name
#     def printName(self):
#         super().showDetails(self.name)
#         print('Course is ')
# class Faculty (Branch):
#     def __init__(self,Math):
#         self.math = Math
#
#     def printFac(self):
#         super().showDetails(self,self.math)
#
#
#
# engineering = Course('Engineering')
# engineering.printde()
#
# mechanical = Branch('Mechanical')
# mechanical.printBranch()
#
# yogesh = Student('Yogesh')
# yogesh.printName()
#
# teacher = Faculty('Deepak')
# teacher.printFac()


# class University:
#     def __init__(self, uname):
#         self.uname = uname
#
#     def detailes(self):
#         print("University name : ", self.uname)
#
#
# class Course(University):
#     def __init__(self, uname, cname):
#         University.__init__(self, uname)
#         self.cname = cname
#
#     def detailes(self):
#         print(f"I did {self.cname} course from {self.uname}")
#
#
# class Branch(University):
#     def __init__(self, uname, branch):
#         University.__init__(self, uname)
#         self.branch = branch
#
#     def detailes(self):
#         print(f"I studied {self.branch} from {self.uname}")
#
#
# class Student(Branch, Course):
#     def __init__(self, branch, cname, uname, name):
#         self.name = name
#         Branch.__init__(self, branch, uname)
#         Course.__init__(self, cname, uname)
#
#     def detailes(self):
#         print(f"I am {self.name} as a student . i'm doing {self.branch} course is {self.cname} from {self.uname}")
#
#
# class Faculty(Branch):
#     def detailes(self):
#         print("faculty")
#
#
# u1 = University("IIT")
# u1.detailes()
#
# c1 = Course("python", "IIT")
# c1.detailes()
#
# b1 = Branch("Computer Science", " IIT ")
# b1.detailes()
#
# s1 = Student("CSE", "Big Data", "BIT", "venkat")
# s1.detailes()


# class University(object):
#     def __init__(self,u_name) -> None:
#         self.univ_name=u_name
#         print(f"(classuniv) The name of the university is {self.univ_name}")
#
# class Course(University):
#     def __init__(self, u_name,c_name) -> None:
#         self.course=c_name
#         self.university=u_name
#         University.__init__(self,u_name)
#         print(f"(classcourse) the course is {self.course}, university name is {self.university}")
#         # return super().show_detail(u_name)
#
# class Branch(University):
#     def __init__(self, u_name,b_name) -> None:
#         self.university=u_name
#         self.branch=b_name
#         University.__init__(self,u_name)
#         print(f"(classbranch)  branch is {self.branch} and university is{self.university}")
#         # return super().show_detail(u_name)
#
# class Student(Course,Branch):
#     def __init__(self,u_name,c_name,b_name,s_name) -> None:
#         self.university=u_name
#         self.student_name=s_name
#         self.course=c_name
#         self.branch=b_name
#         Course.__init__(self,u_name,c_name)
#         Branch.__init__(self,u_name,b_name)
#         print(f"Student of branch: \n\tstudent: {self.student_name} \n\tbranch: {self.branch} \n \t University: {self.university} \nstudent of class course: \n\t student: {self.student_name} \n\t course: {self.course} \n\t University: {self.university}")
#         # return super().show_detail(u_name, c_name)
#
# class Faculty(Branch):
#     def __init__(self, u_name,b_name,f_name) -> None:
#         self.faculty_name=f_name
#         self.university=u_name
#         self.branch=b_name
#         Branch.__init__(self,u_name,b_name)
#         print(f"(facultyclass) faculty: {self.faculty_name}, branch: {self.branch} , university: {self.university}")
#         # super().__init__(u_name, b_name)
# f1=Faculty("Pokhariya University","Biratnagar","Computer-Engineering")
#
# s1=Student("Pokhariya University","Computer-Engineering","Biratnagar","Abhishek Mehta")
# s1.show_detail()


#  Diamond Inheritance Problem