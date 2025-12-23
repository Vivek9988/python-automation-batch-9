class Car:
    #magic method to initiate the obj
    def __init__(self, brand, model, string):
        self.brand = brand
        self.model = model
        self.string= string

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")


class Truck:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("turn with the more mielage")


car = Car("Ford", "Figo")
boat = Boat("Ibiza", "I20")
truck = Truck("Mahindra", "T20")

for x in (car, boat, truck):
    x.move()
