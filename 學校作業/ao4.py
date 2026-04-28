n = int(input())

books=[]


for i in range (n):
    name = input()
    books.append(name)

query= input().lower()
found = False#初始狀態，會用此方法，原因，需要一個穩定的被動，當今天沒有發生其他的方法，就使用這個
#當今天找不到書時，是看完所有的書，然後回報，所以需要初始狀態，不然他會每一本書都抱一次
for i in books:
    if query in i.lower():#這裡做小寫畫不會影響書名
        print(i)
        found =True  #這裡是防止觸發下面的if 
if found == False:
           print("No match found")