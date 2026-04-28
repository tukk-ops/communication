
goal = int(input())

raw_input = input()
num_strings = raw_input.split()

xx = []

for s in num_strings:#將清單裡的字串挑出轉成整數，加入清單
    number = int(s)   
    xx.append(number) 

count = 0

z = len(xx)
for i in range(z): #加總
    count = count + xx[i]
print(f"Total: {count}") 

if count >= goal: #判定有無到達目標
    print("Goal Achieved!")
else:
    print("Keep Walking!")

#此題重點，split()出來的東西，是一個清單，不是個單個 單個的字串，int()只能一次處理一個，所以
#用迴圈將其拆開，並同時轉成字串，放入清單作家總