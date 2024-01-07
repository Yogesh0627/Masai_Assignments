
class A:
    def display(self):
        print('Display of A')

class B(A):
    def display(self):
        print('Display from B')

class C(A):
    def display(self):
        print('Display from C')
    def show(self):
        print('Hii from C Class')

class D(B,C):
    pass

d1 = D()

d1.display()

Abstraction_Demo = open('../Abstraction/Abstraction_Demo.py', 'x')