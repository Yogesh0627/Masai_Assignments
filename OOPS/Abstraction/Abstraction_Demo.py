from Abstract_Class import Vehicle
class Bike(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print('Start With Kick')

class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print('Self-Start')

class Car(Vehicle):
    def __init__(self,n,x):
        super().__init__(n)
        self.gears = x
    def start(self):
        print('start with key')
