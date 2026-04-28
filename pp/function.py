#方法函數，只需在後面加上括號即可使用 
#如果定義誇號裡面有要寫入東西，記得在使用時誇號裡要有數值
#def say_hello():
    #print("heelo")
#say_hello()


#return會回傳一個值，可是這個值需要一個變數來接收他 
#def add(x,y):
        #return x+y
#answer = add(5,3)
#print(answer)


##變化做出改變後的值為一個變數，然後return，但要有print()才能打出東西
#def big_name(first,last):
        #first = first.capitalize()
        #last = last.capitalize()
        #return first + " "+ last
#print(big_name("john"+"rwer"))


###預設引數(預設值)，他必寫在其他變數(沒有預設值)的後面
#def big_name(first,last="jr"):



 #####在呼叫時寫 big_name(first="John", last="Smith")，這時候的 first= 和 last= 就是關鍵字參數
#如果沒有關鍵字參數，你必須嚴格遵守 def 定義的順序。有了它，你可以隨便換，順序不再是問題 (Order doesn't matter)：