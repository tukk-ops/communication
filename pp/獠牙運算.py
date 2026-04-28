#獠牙運算
#:=，將值分配給變數

happy =True
#print(happy)
print(happy :=True)
#單純的print(happy =True)，無法在這樣的禽況下做賦值，但如果用:=(獠牙運算)，就可以

foods =[]      # food = input("")
while (food := input(""))!= "quit":   #縮減要不要停止那行，要記得用()，才能把輸入的東西拿去做比較(不然會是拿true)
    #if food =='quit':
        #break
    foods.append(food)

print(foods)

#food := input(...) #會先執行輸入並存進 food。

#接著它會直接拿這個結果去跟 "quit" 比較。

#這時候它的「值」就很重要了，因為它直接決定了 while 括號內的結果是 True 還是 False。
