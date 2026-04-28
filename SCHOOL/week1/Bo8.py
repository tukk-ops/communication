class Transport:
    def __init__(self,kg):
        self.kg = kg
    def calculate_cost(self):
        return  0

class  Truck(Transport):
    def __init__(self, kg):
        super().__init__(kg)
    def calculate_cost(self, distance):
        return distance * 20

class Drone(Transport):
    def __init__(self,kg):
        super().__init__(kg)
    def calculate_cost(self, distance):
        return distance * 5 + 50


n = int(input())
park = []

for i in range(n):
     data = input().split()
     name = data[0]
     kg= int(data[1])
     if name  == "Truck":
         car = Truck(kg)
         park.append(car)
     elif name == "Drone":
         car = Drone(kg)
         park.append(car)
test = int(input())

for i in  range(test):
    ddata = input().split()
    kg = int(ddata[0])
    distance = int(ddata[1])
    cost = -1
    for chch in park:
        if kg <= chch.kg:
            if cost == -1 or cost > chch.calculate_cost(distance):
                    cost = chch.calculate_cost(distance)    
    
    if cost != -1:
        print(f"Lowest Cost: {cost}")
    else:
        print("No transport available")


