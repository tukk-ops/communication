n = int(input())
vv = {}
for _ in range(n):
    data = input().split()
    first = data[0]
    name = data[1]
    Value = int(data[2])#分解指令
    if first in vv:
        vv[first]+=Value#一樣會跌家
    else:
        vv[first] = Value#存入

max_first = ""
max_val =0

for cat in vv:
    val = int(vv[cat])#意思：去字典 vv 裡面，查查看 cat (例如 'Fruit') 這個類別對應的 值 (Value) 是多少。
    if val >max_val:
        max_val = val#值得更新
        max_first =cat#列更新

print(f"Highest: {max_first} ({max_val})")

for cat in sorted(vv):
    print(f"{cat}: {vv[cat]}")