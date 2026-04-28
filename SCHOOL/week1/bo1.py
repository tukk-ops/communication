class member:
    def get_discount(self):
        return 1.0
class VIPMember(member):
    def get_discount(self):
        return 0.8
class GoldMember (member):
    def get_discount(self):
        return 0.7    


test = int(input())
for i in range(test):
    data = input().split()
    level = data[0]
    mm =int(data[1])
    if level == "Normal":
        pp = member()
        print(int(pp.get_discount()*mm))
    elif level =="VIP":
        pp = VIPMember()
        print(int(pp.get_discount()*mm))
    else :
        pp = GoldMember()
        print(int(pp.get_discount()*mm))
    
