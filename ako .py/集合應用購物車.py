goods =[]
prices=[]
while True: 
    good = input()
    if good.lower() == "q":
        break
    price = input()
    goods.append(good)
    prices.append(price)
fruits = ['蘋果', '香蕉', '橘子']
for index,good in enumerate(goods):
    print(f"第{index+1}個商品，{good},m:{prices[index]}")
total = sum(prices)
print(f"total:{total}")