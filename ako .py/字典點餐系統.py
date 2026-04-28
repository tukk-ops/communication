menu = {
    "apple":290
    ,"bannna":920
    ,"cat":890
    ,"dvd":10
    ,"ete":345
}
print("menu")
print("-------------")
cart =[]
t= 0
for item, price in menu.items():
    print(f"{item}:{price}")
while True:
    food = input()
    if food == "q":
        break
    elif menu.get(food) is None:
        print("no")
    else:
        cart.append()
        t+=menu.get(food)
        print(food,end=" ")
        print(f"t:{t}")