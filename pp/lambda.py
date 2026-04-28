#lamba 函式，一航寫完
#只有一個表達式，只需要用一次，或短時間
#簡單的函數解決特定的任務
def double(x):
    return x*2
print(double(10))


double2 = lambda x: x*2
print(double2(50))

bxb = lambda x,y:x*y
print(bxb(3,2))


#lamba的條件與據
result = lambda x:f"{x}是偶數"if x%2 ==0 else f"{x} 是奇數"

print(result(15))

#處理字串
