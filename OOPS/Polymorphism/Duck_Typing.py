class Duck:
    def swim(self):
        print('I am a duck and i can swim')
    def speak(self):
        print('Quack Quack')

class Dog:
    def swim(self):
        print('I am a dog and i can swim')

    def speak(self):
        print('woof woof')
class Person:
    def speak(self):
        print('blah blah blah')
def display(obj):
    obj.swim()
    obj.speak()
    print('Inofrmation Displayed')

d1 = Duck()
dog = Dog()
display(d1)
p = Person
display(p)