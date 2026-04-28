#物件(object) 是類別(class)的實例

#車  (class)
#每一台的車子(object)


class car :#                                 提供我們欲製造物件

    wheel = 4 #                              類別變數，定義在 class 內，但在 def 之外
           #car1.wheel即可使用

    def __init__(self,brand):#                不同的情況，會有不同的屬性，self.make 即可創建
        self.make = brand#                           屬性，自己要提供

    def drive(self):
        print(f"{self.make},driving")

    def stop(self):
        print(f"{self.make},stop in the line")



car1 = car("tt")                        #tt是屬性，car1是物件
print(f"品牌:{car1.make}")#有self.才可以在其他地方做使用
car1.drive()
#簡單來說，self 就好比是在類別內部使用的**「代名詞」，而 car1 是在外面呼叫時的「真實名字」

