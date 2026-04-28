def Payment(money,pp):
    money= int(money*1.1)
    one = int(money//pp)
    print(f"Total: NT${money}, Per person: NT${one}")

data = input().split()
pp = int(data[0])
money = int(data[1])
Payment(money,pp)