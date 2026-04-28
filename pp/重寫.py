class animal:

    def eat (self):
        print("這個動物震在吃東西")


class mammel (animal):
    def hi (self):
        print("我是哺乳類")




class rabbit(mammel):
    def eat (self):
        print("兔子在吃東西")


class dog(mammel):
    def eat(self):
        print('狗吃東西')



rabbit9 =rabbit()
rabbit9.eat()   #會覆蓋掉父輩的方法
dog22 = dog()
dog22.eat()
m = mammel()
m.eat()