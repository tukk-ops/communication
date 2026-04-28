
class Effect:
    def __init__(self,duration):
        self.duration =  int(duration)
    def apply(self, character):
        self.duration -= 1

class Poison(Effect):
    def apply(self,character):
        character.hp -= 10
        super().apply(character)
class  Regen(Effect):
    def apply(self,character):
        character.hp += 15
        super().apply(character)

class Character:
    def __init__(self,hp):
        self.hp = int(hp)
        self.effects = []
    def add_effect(self,effect):
        self.effects.append(effect)
    def next_turn(self):
        for effect in self.effects:
            effect.apply(self)
        self.effects =[e for e in self.effects if e.duration >0]#跟新清單裡面效果的回合，大於零就在紀錄一次沒有就不記錄
        print(f"Current HP: {self.hp}")

hp = int(input())
player = Character(hp)
test = int(input())
for i in range(test):
        data = input().split()
        if data[0] =="add":
            level = data[1]
            d = int(data[2])

            if data[1] == "Poison":
                player.add_effect(Poison(d))
            elif data[1] == "Regen":
                player.add_effect(Regen(d))
        elif data[0] =="turn":
            player.next_turn()


 