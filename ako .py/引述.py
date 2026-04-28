#物件當成引術

class car:
    color =  None

def change_color(car,color):
    car.color = color

car0 = car()
car1 = car()

print(car1.color)
change_color(car1,"red")
print(car1.color)

#建立好的物件，不用整個去修改，而是用引數的方式去修改，重複使用已經建立好的物件
#1. 位置決定了它的身份
#請看你截圖中的程式碼縮排（Indentation）：

#實例方法 (Method)：定義在 class 的裡面（縮排一格）。Python 會自動把調用者傳給第一個參數，慣例命名為 self。

#外部函數 (Function)：定義在 class 的外面（沒有縮排）。它跟這個類別沒有「血緣關係」，它只是一個獨立的工具箱。

 #這裡是在：這是一個「外部函數 (Function)」，而不是「類別方法 (Method)」。
 #self 專指「類別內部的自己」。
 #它不是自動傳入的：因為 change_color 在類別外面，當你呼叫它時（例如 change_color(car1, "red")），你必須手動把 car1 這個物件丟進去。
 #寫 self：代表「這是我（物件）具備的功能」。