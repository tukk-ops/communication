class Access:
    def __init__(self,name_list):
        self.name_list = name_list
    def catch(self,n):
        try:
            n =int(n)
            print(self.name_list[n])
        except  ValueError:
            print("Error: Invalid index type")
        except IndexError:
            print("Error: Index out of bounds")

data  = input().split()
obj = Access(data)#把單一個清單accseec化
    
n = int(input())
for _ in range(n):
    query = input()#不用刻意轉成整數，因為定理有寫try
    obj.catch(query)


