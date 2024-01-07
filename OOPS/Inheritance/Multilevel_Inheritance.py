'''
In Multiple Inheritance we don't have more than one parent
we can derived from child classes as well
we can inherit from derive class as well
'''

# class Human:        # ===> Parent Class (Grand-Parent)
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
#
# # Child Class
# class Boy(Male):        # ===> Child Class 2
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         print('I talk a lot')
#
# yogesh = Boy()

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[

# if want to acess the method having the same name as in parent than use super or another syntax

# class Human:        # ===> Parent Class (Grand-Parent)
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
#
# # Child Class
# class Boy(Male):        # ===> Child Class 2
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         # super().talk()
#         Human.talk(self)
#         print('I talk a lot')
#
# yogesh = Boy()
# yogesh.talk()


# {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{


'''
Now Attributes
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
#
#
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
#
# # Child Class
# class Boy(Male):        # ===> Child Class 2
#     def drive(self):
#         print('I Drive Bike')
#     def talk(self):
#         # super().talk()
#         Human.talk(self)
#         print('I talk a lot')
#
# yogesh = Boy(1)
# yogesh.talk()

# whilke acessing init function it will check the first inh\it of its parent and than goes on upper
# upper and lastly it will check in object
# if it find init in any parent class than that init will run


class Human:        # ===> Parent Class (Grand-Parent)
    def __init__(self,heart):
        print(f'Human init Called')
        self.heart=heart
        self.num_nose = 1
        self.num_ear = 2
        self.num_eye = 2
    def work(self):
        print('I Can Work')
    def walk(self):
        print('I Can Walk')
    def eat(self):
        print('I Can Eat')
    def talk(self):
        print('I Can Talk')


class Male (Human): # ===> Child Class

    def __init__(self,name,language,heart):
        print('Male init run')
        Human.__init__(self,heart)
        self.name = name
        self.language = language

    def think(self):
        print('I Can Think')
    def earn(self):
        print('I Can Earn')
    def married(self):
        print('I Can Married')
    def drive(self):
        print('I Can Drive')


# Child Class
class Boy(Male):        # ===> Child Class 2
    def drive(self):
        print('I Drive Bike')
    def talk(self):
        # super().talk()
        Human.talk(self)
        print('I talk a lot')

yogesh = Boy('Yogesh','python',1)
# yogesh.talk()

print(yogesh.heart)


