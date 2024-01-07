'''
Method overloading means we are defining multiple methods / many methods
with same name but different arguments in a same class
'''


'''
1. Compile Time Polymorphism
2. Python doesn't supports
3. occure in same class 
4. mulitple methods should be in same
class with same name but with different number of parameters)

'''

'''
By default python does not support overloading while
some other landuages can , but we can 
achieve it through differnet ways one way is 

1. Default Arugements 
2. arguments (args)
'''
# class Demo:
#     def add(self,a,b):
#         return a+b
#
#     def add(self,a,b,c):
#         return a+b+c
# d = Demo()
# print(d.add(5,5))
# print(d.add(5,5,5))
#

'''
# default arguements

class Demo:
    # def add(self,a,b):
    #     return a+b

    def add(self,a,b,c=0): # making c as a default arguement
        return a+b+c
d = Demo()
print(d.add(5,5))
print(d.add(5,5,5))
'''


'''
#  args

class Demo:
    # def add(self,a,b):
    #     return a+b

    def add(self,*args): # making args because don't know how many args we gonna pass
        total = 0
        for i in args:
            total += i
        return total

d = Demo()
print(d.add(5,5))
print(d.add(5,5,5))

'''


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

''' Method Overriding '''
'''
Method overriding is used in implementation in inheritance only 
minimium 2 classes required.

In parent class we have a method then the same method in child class 
but in its own way ( no of Arguements and parameters are same)
diferent in locations as they are in different classes
'''

'''
1. Runtime Polymorphism
2. Python Supports
3. Occur in Inheritance only
4. method have same name , same number of parameters
different in location 

'''
class Father:
    def sleep(self):
        print(f'sleeps froom 10 PM to 5 AM')
    def eating(self):
        print('Eating')

class Son(Father):
    def sleep(self): # this is known as method overridng because we are overwriting the parents method
        print(f'sleeps from 2 AM to 10 AM')
        super().sleep()

s1 = Son()
s1.sleep()