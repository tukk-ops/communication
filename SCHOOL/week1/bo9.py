class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def cal(self):
        try:
            x=int(self.x)
            y =int(self.y)
            new_t = x // y
            print(new_t)
            return new_t
        except  ValueError:
            print("Error: Invalid input")
        except  ZeroDivisionError:
            print("Error: Division by zero")

n =int(input())
for i in range(n):
    data  = input().split()
    m = data[0]
    n  = data[1]   
    big_g = Calculator(m,n)
    big_g.cal()
#請注意這題要讓他能跑出價值錯誤，是字母轉整數的時候，才會抱錯，然後他要偵測
#這個錯，就必須要在他的try裡面