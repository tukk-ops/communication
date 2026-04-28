n = int(input())

for _ in range(n):
    line = input().split(",")
    #以,為間隔去區分讀取到的數字
    t = float(line[0])
    s = int(line[1])

    if s <=100:
        for j in range(1,s+1):
            t = t + (j* 2.71828)#主要地回的地方
    
    print(f"{t:.4f}")

#地回，以舊的值去加上偏差，得出書新的值
