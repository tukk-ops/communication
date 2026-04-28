#核心概念：map(function, iterable)
#(函數，方法)
store = [
    ("short",20),
    ("tshort",30),
    ("eso",20),
]
#to_eu = lambda data : (data[0],data[1]*0.82)

##store_eu = list(map(to_eu, store))
store_eu = list(map(lambda store: (store[0], store[1]*0.82),store))
print(store_eu)

#省略了for去讀清單裡的東西，再套入公式，加入清單，打印
#Map 會抓出清單裡面的東西嗎，再丟入lambda，再包裝成清單嗎
