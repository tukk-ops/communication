#建立子類別可以指定父類別


class animal:
    alive = True

    def eat (self):
        print("這個動物震在吃東西")
    def sleep (self):
        print("這個動物震在睡覺")

class rabbit(animal):
    def jump(self):
        print("動物jjjjump")


rabbit2 = rabbit()
rabbit2.eat()
rabbit2.jump()

#繼承，他可以使用上一個東西方法，屬性，然後拿去做使用