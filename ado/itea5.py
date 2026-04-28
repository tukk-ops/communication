#data = input().split()
#ee =set()
#for char in data :
#   ee.add(char)

#print(*ee)
#Set 的特性：會自動去重，且不保證順序。
dd =[]
data = input().split()

if len(data) <= 1000:
    for char in data :
        if char.lower() not in dd:
            dd.append(char.lower())
print(*dd)