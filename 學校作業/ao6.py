class Item:  
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)

class ShoppingCart:
    def __init__(self):
        self.vv = []#維護清單
        
    def add_item(self, item):
        self.vv.append(item)#加入清單
                
    def remove_item(self, name):
        
        for i in range(len(self.vv)):
            if self.vv[i].name == name:
                self.vv.pop(i)
                break #暫停並移除
                
    def get_total(self):
        total = sum(Item.price for Item in self.vv)#@這裡去做挑屬性
        return total

cart = ShoppingCart()

n = int(input())

for i in range(n):
        data = input().split()
        go = data[0]

        if go == "add":
            name = data[1]
            price = data[2]
  
            new_item = Item(name, price) 
            cart.add_item(new_item)
            
        elif go == "remove": 
            name = data[1]
            cart.remove_item(name)
            
        elif go == "total":
            print(f"Total: {cart.get_total()}")
            
#他是(名字,價格)這樣存進去的