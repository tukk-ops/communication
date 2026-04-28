row0 = input().split()
row1 = input().split()
row2 = input().split()

grid = [row0, row1, row2]


win = False
#列嶼行的連線，
for i in range(3):##橫，    前面的列不動，串起來是一橫
    if grid[i][0] == grid[i][1]==grid[i][2]:
        win = True

for i in range(3):#直，  後面的不動，串起來是1
    if grid[0][i] == grid[1][i] ==grid[2][i] :
         win = True
#兩條斜線
if grid[0][0]==grid[1][1]==grid[2][2]:
    win = True
if grid[0][2]==grid[1][1]==grid[2][0]:
    win = True
if win:
    print("True")
else:
    print("False")




#第一個索引 [0], [1], [2] 變動： 代表你跨越了不同的列（上下移動）。

#第二個索引 [i] 固定： 代表你始終待在「第 i 行」。

#上下移動但維持在同一行，連起來就是一條直線。