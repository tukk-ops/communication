# duck typing
#類別不如他傭有的方法和屬性重要
#如果一個物件傭有足夠多的方法和屬性，就算不屬於這個類別，還是會把它當作這個類別處理

class chicken:
    def walk(self):
        print("雞在走路")

    def talk(self):
        print("咕咕咕咕咕咕")
        
class duck:
    def walk(self):
        print("鴨在走路")

    def talk(self):
        print("呱呱呱呱呱")

#即使沒有記陳關係，也可以當作是農依類別作使用   

class person():
    def catch(self,duck):
        duck.walk()#Python 會自動把 duck 這個實體當作第一個參數傳進去。所以實際上執行的是 walk(duck)。
        duck.talk()


duck_1=duck()
#chicken0 =chicken()
person1 = person()
person1.catch(duck_1)#今天是物件才能完美啟動方法，person1和duck_1才能自動填入(self,duck)，去使用duck方法(duck_1=duck())





#步驟：他先寫了 chilken = Chilken() (注意有括號)，這代表他根據「雞」的藍圖蓋出了一隻「真正的雞」。再利用真正的雞，傳入person.catch(...)
