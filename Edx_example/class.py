class Car(object):
    def _init_(self,make,model,color):
        self.make = make;
        self.model = model;
        self.color = color;
        self.owner_number = 0
    def car_info(self):
        print("make",self.make)
        print("model",self.model)
        print("color",self.color)
        print("no of owners",self.owner_number)
    def sell(self):
        self.owner_number = self.owner_number + 1

make = "BMW"
model = "M3"
color = "silver"
my_car = Car(make,model,color)

my_car.car_info()
for i in range(5):
    my_car.sell()
my_car.car_info()
