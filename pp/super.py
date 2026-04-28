class rectengle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        print("矩行以初始化")

class square(rectengle):
    def __init__(self, length, width):
        super().__init__(length, width) 
        print("正方形以初始化")

class cube (rectengle):#要注意它繼承的是哪一個區塊的類別
    def __init__(self, length, width,tall):
        super().__init__(length, width)
        self.tall = tall
        print(f"立方體的長寬高{length}.{width}.{tall}")


cube12 = cube(10,20,30)