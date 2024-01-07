'''
there are total five types of inheritance
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Heirarchy Inheritance
5. Hybrid Inheritance
'''


'''
Single Inheritance

1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism 
'''


# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')

#  Accessing or inherting parent methods in child methods
# class Male(Human):
#     pass
#
# yogesh = Male()
#
# yogesh.eat()
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
# #  OverRiding parent methods in child methods
# class Male(Human):
#     def eat(self):
#         print('I Eat Rajma Chawal')
# yogesh = Male()
#
# yogesh.eat()

# class Human:
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')

#  Using both methods before overriding parent method and after overriding in child class with
#  With th ehelp super function super function used to acess the attributes and methos of parent in child
# class Male(Human):
#     def eat(self):
#         super().eat()
#         print('I Eat Rajma Chawal')
# yogesh = Male()
# yogesh.eat()

# class Human:
#     def __init__(self):
#         self.numEyes = 2
#         self.numEars = 2
#         self.numNose = 1
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')

#  Accessing parent Attributes through Child object
# class Male(Human):
#     def eat(self):
#         print('I Eat Rajma Chawal')
# yogesh = Male()
#
# yogesh.eat()
#
# print(yogesh.numEars)


# class Human:
#     def __init__(self):
#         self.numEyes = 2
#         self.numEars = 2
#         self.numNose = 1
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')

#  If consutructor is defined in child class then it is mandatory to used
#  super function in child class to access those attributes which are defined in
#  parents class constructor
# class Male(Human):
#     def __init__(self):
#         super().__init__()
#         self.legs = 2
#         self.hands=2
#     def eat(self):
#         print('I Eat Rajma Chawal')
# yogesh = Male()
#
# yogesh.eat()
#
# print(yogesh.numEars)



# class Human:
#     def __init__(self,heart):
#         self.numEyes = 2
#         self.numEars = 2
#         self.numNose = 1
#         self.numHeart = heart
#     def work(self):
#         print('I Can Work')
#     def walk(self):
#         print('I Can Walk')
#     def eat(self):
#         print('I Can Eat')
#     def talk(self):
#         print('I Can Talk')

#  Incase a variable need to paas in parent than it is passed in to super function in
#  and then it same pass into the constructor of child like below mentioned
# class Male(Human):
#     def __init__(self,heart,name):
#         super().__init__(heart)
#         self.name = name
#     def eat(self):
#         print('I Eat Rajma Chawal')
# yogesh = Male(1,'yogesh')

# yogesh.eat()
# print(yogesh.numHeart)
# print(yogesh.numEars)





class Human:  # Super Class / Parent Class
    def __init__(self,heart):
        self.heart = heart
        self.ears = 2
        self.nose = 1
    
    def walk(self):
        print('I can walk')
    def eat(self):
        print('I can Eat vegetarian only')

    def sleep(self):
        print('I can sleep parent')

class Male: # derived Class
    def __init__(self , hands):
        self.legs = 2
        self.eyes = 2
        self.hands = hands
    def canWork(self):
        print('I can Work')
    def sleep(self):
        print(' I sleep Long from male')

class Boy(Male,Human):
    def __init__(self,name,age,hands , heart):
        Male.__init__(self,hands)
        Human.__init__(self,heart)
        self.name = name
        self.age = age


deepak = Boy('Heera',22,2,1)
# deepak.sleep()
# Human.sleep(deepak)
# deepak.eat()
print(deepak.nose)

# print(Male.mro())