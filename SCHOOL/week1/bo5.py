class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp =int(hp)
        self.atk= int(atk)
    def attack(self,target):#定義攻擊目標
        target.take_damage(self.atk)#目標受到本屬性的傷害，並使用take_damage配合，使目標能啟動函數

    def take_damage(self,amount):#敵人的self.atk，傳入這裡，扣掉
        self.hp -= amount
    
class Warrior(Hero):
    def __init__(self, name, hp, atk,armor):
        super().__init__(name, hp, atk)#繼承父輩屬性
        self.armor = int(armor)

    def take_damage(self, amount):#這裡敘寫父輩的take_damage
        damage = max(0,amount-self.armor)
        super().take_damage(damage)
class Mage(Hero):
    def __init__(self, name, hp, atk,mana):
        super().__init__(name, hp, atk)
        self.mana = int(mana)
    def attack(self,target):
        if self.mana >= 10:  #如果大於10就使用雙被攻擊
            self.mana -= 10  
            target.take_damage(2 * self.atk) 
        else:
            target.take_damage(self.atk) 

data = input().split()
p1 = Warrior(data[1],data[2],data[3],data[4])
data2 = input().split()
p2 = Mage(data2[1],data2[2],data2[3],data2[4])
n = int(input())
for i in range(n):
    move = input().split()
    if move[0] == data[1]:
        p1.attack(p2)
    else:
        p2.attack(p1)
print(f"{p1.name} HP: {p1.hp}")
print(f"{p2.name} HP: {p2.hp}")