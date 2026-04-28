class Appliance:
    def __init__(self,name,power):
        self.name = name
        self.power = int(power)
    def use(self,hours):
        return self.power * hours
    
class SmartAC(Appliance):
    def __init__(self, name, power,temp):
        super().__init__(name, power)
        self. temp = int(temp)
    def use(self,hours):
        if self.temp < 25:
            np = self.power*1.2
            return np*hours
        else:
            return self.power * hours
class SmartTV(Appliance):
    def __init__(self, name, power):
        super().__init__(name, power)
    def use(self, hours):
            np = self.power*0.9
            return np*hours


n =int(input())
for i in range(n):
    data = input().split()
    name= data[0]
    if name == "AC":
        ac = SmartAC(data[1],data[2],data[3])
        x = int(ac.use(int(data[4])))
        print(f"{data[1]} used {x} Wh")
    elif name =="TV":
        tv = SmartTV(data[1],data[2])
        x = int(tv.use(int(data[3])))
        print(f"{data[1]} used {x} Wh")
    elif name =="Normal":
        nn = Appliance(data[1],data[2])
        x = int(nn.use(int(data[3])))
        print(f"{data[1]} used {x} Wh")

