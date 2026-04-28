data = input().split()#把自切開，自動放入清單

num =[]
for char in data:
    if char =="x":
        num.append(10)#處理好10 這個數字
    else:   
        num.append(int(char))#其他字轉整數

first_sum =[]
total_1 = 0
for n in num :
    total_1+=n##只是為了找和，所以直接蝶家就好
    first_sum.append(total_1)

second_sum =[]
total_1 =0 
for i in first_sum:
    total_1 += i
    second_sum.append(total_1)


if second_sum[-1] %11 ==0:
    print("YES")
else:
    print("NO")


#isbn的結構，由前面疊加而來，第二航由第一航建構(兩兩相加)
#需要紀錄第一航的每一個數才可以做第二航
#需解決的問題/1.接著進行第一次的累加，使得第二位數成為第一位數到第二位數的和，第三位數為第一位數到第三位數的累加和...
#2.倘若此識別碼為 11 的倍數，則此 ISBN 碼為合法的。
#解法這行的第5位數等於前一列的1-5為樹枝和，跟第二列要是11的倍數