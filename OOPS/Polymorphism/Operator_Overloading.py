'''
Double Underscore , Magic Method , Dunder Method

print(1+2) ==> 3
print('1' + '2') => 12

'''

class ComplexNumber:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i


c1= ComplexNumber(1,2)
c2= ComplexNumber(2,3)
# print(c1+c2) # ==> Error


# now adding by operator overloading / dunder method

# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
#
#     def __add__(self, other):
#         # return str(self.real + other.real) + '+' + str(self.imaginary + other.imaginary) +'i'
#         return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
# c1= ComplexNumber(1,2)
# c2= ComplexNumber(2,3)
#
# print(c1+c2)


''' ==> String ==> '''

# class string:
#     def __init__(self,word_one):
#         self.word_one = word_one
#         # self.word_two = word_two
#
#     def __add__(self, other):
#         return self.word_one+other.word_one
# s1 = string('Yogesh')
# s2 = string(' Chauhan')
# # print(s1+s2) == >Giving Error unsuported operand without dunder method
#
# #  after applying dunder method
# print(s1+s2)

#  Practice Question Appply overloading on greater than method


class GreaterThan:
    def __init__(self, Age_one ):
        self.Age_one = Age_one
        # self.Age_two = Age_two

    def __gt__(self, other):
        return self.Age_one > other.Age_one
a1 = GreaterThan(15)
a2 = GreaterThan(18)
# print(a1 > a2)
if (a1 > a2):
    print('a1 will pay the bill')
else:
    print('a2 will pay the bill')


