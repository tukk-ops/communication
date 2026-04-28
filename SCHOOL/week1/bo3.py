class Vehicle:
    def __init__(self,plate):
        self.plate = plate
    def calculate_toll(self):
        return 40
    
class  Truck(Vehicle):
    def __init__(self, plate):
        super().__init__(plate)
    def calculate_toll(self,weight):
       tt=  super().calculate_toll() +(int(weight)*10)
       return tt
    
class Bus(Vehicle):
    def __init__(self, plate):
        super().__init__(plate)
    def calculate_toll(self,po):
        total = super().calculate_toll() +(int(po)*5)
        return total

test = int(input())
for i in range(test):
    data = input().split()
    level = data[0]
    plate =  data[1]
    

    if level == "Vehicle":
        car = Vehicle(plate)
        print(f"{plate}: ${car.calculate_toll()}")
    elif level =="Truck":
        t_pp = data[2]
        car = Truck(plate)
        print(f"{plate}: ${car.calculate_toll(t_pp)}")
    else :
        t_pp = data[2]
        car = Bus(plate)
        print(f"{plate}: ${car.calculate_toll(t_pp)}")