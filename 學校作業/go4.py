book = int(input())
app = []
for i in range(book):
    name = input().strip()
    app.append(name)  #分批加入清單
found = False
c=input().lower()
for i in range(len(app)): #依照書本數量做迴圈
    if c in app[i].lower():#app[i] 代表取出列表中的第 i 個元素。因為你存進去的是書名，所以 app[i] 取出來的就是一個字串 (String)
         print(f"{app[i]}")
         found = True 
        
if found == False:  
        print("No match found")
        
#如果你直接在迴圈裡面寫 else: print("No match found")，程式每看到一本「不符合」的書就會印一次
#當迴圈跑完後，我們去檢查 found。如果它還是 False，代表剛剛那圈搜尋中「從來沒有任何一本書」觸發過 found = True，這時我們才印出 No match found。
#所以當有搜尋到，就會記錄，避免印出"No match found"