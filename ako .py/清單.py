import time

my_time = int(input())

for i  in range(my_time,0,-1):
    s = i % 60 
    m = i //60 %60#要找出有幾分鐘
    print(f"{m:.00f}:{s:.00f}")
    time.sleep(1)
print("out")