'''
Inheriting properties or attributes from more than one parent
'''

# Parent One
# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')
#
# #  Accessing or inherting from Both parents to child
# # Parent Two
# class Male:
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#
#
# # Child Class
# class Boy(Human,Male):
#     pass
#
# yogesh = Boy()
#
# yogesh.drive()


# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')
# 
# #  Accessing or inherting from Both parents to child and Overriding
# # Parent Two
# class Male:
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
# 
# 
# # Child Class
# class Boy(Human,Male):
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         print('I talk a lot')
# 
# yogesh = Boy()
# 
# yogesh.drive()
# yogesh.talk()


# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')
#
# #  Accessing or inherting from Both parents to child and Overriding
# # Parent Two
#
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#
# # Using both methods before overriding parent method and after overriding in child class with
# #  With th ehelp super function super function used to acess the attributes and methos of parent in child
# class Male:
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#
#
# # Child Class
# class Boy(Human,Male):
#     def drive(self):
#         super().drive()
#         print('I Drive Bike')
#     def talk(self):
#         super().talk()
#         print('I talk a lot')
#
# yogesh = Boy()
# yogesh.drive()
# yogesh.talk()


# ...............................................................................

# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')
#
# #  Accessing or inherting from Both parents to child and Overriding
# # Parent Two
#
# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# # Using both methods before overriding parent method and after overriding in child class with#  With th ehelp super function super function used to acess the attributes and methos of parent in child
# class Male:
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#
#
# # Child Class
# class Boy(Human,Male):
#     def drive(self):
#         super().drive()
#         print('I Drive Bike')
#     def talk(self):
#         super().talk()
#         print('I talk a lot')
#
# yogesh = Boy()
# yogesh.drive()
# yogesh.talk()

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


'''
if both class have same type of function and want to execute one function from child then the
execution depends upon the how written of the parent classes order  
'''
#
# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')
#
#
# class Male:
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#     def work(self):
#         print('I Can Cook')
#
#
# # Child Class
# class Boy(Male,Human):
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         super().talk()
#         print('I talk a lot')
#
# yogesh = Boy()
# yogesh.drive()
# yogesh.talk()
# yogesh.work()
# Human.work(yogesh)
# print(Boy.mro())



# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
Attribute Case
'''



# class Human:
#     def __init__(self,heart):
#         self.heart=heart
#         self.num_nose = 1
#         self.num_ear = 2
#         self.num_eye = 2
#
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')


# class Male:
#     def __init__(self,name):
#         self.name= name
#         self.age = 18
#
#     def think(self):
#         print('I Can Think')
#     def earn(self):
#         print('I Can Earn')
#     def married(self):
#         print('I Can Married')
#     def drive(self):
#         print('I Can Drive')
#     def work(self):
#         print('I Can Cook')


# Child Class
# class Boy(Male,Human):
#     def __init__(self,name,language,heart):
#         Human.__init__(self,heart)
#         Male.__init__(self,name)
#         self.language=language
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         # super().talk()
#         print('I talk a lot')
#     def display(self):
#         print(f'hey i am {self.name} and i  work on {self.language}')

# yogesh = Boy('Yogesh','Python',1)
# yogesh.drive()
# yogesh.talk()
# yogesh.work()
# yogesh.display()
