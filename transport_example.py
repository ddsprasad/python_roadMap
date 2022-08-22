class Vehicle(object):
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage



class Bus(Vehicle):
    def seating_capacity(self,no_seats=50):
        # return f'The Seating Capacity of the {self.name} is {no_seats} and its color is {self.color}'
        return f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'

class Car(Vehicle):
    def seating_capacity(self,no_seats=4):
        return f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'

b1 = Bus('godavari',120,5)
c1 = Car('Skoda',180,13)
print(b1.seating_capacity())
print(c1.seating_capacity())