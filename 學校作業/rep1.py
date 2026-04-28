n = int(input())
sdu = []
for i in range(n):
    name = input()#這裡不要做split因為它會自動分列出清單，在後面13行會抱錯，
    sdu.append(name)#目的是要完整的書名加進去，讓後面去照

com = input().lower()
found = False


for i in sdu:
    if com in i.lower():
        print(i)
        found = True
if found == False:
    print("No match found")