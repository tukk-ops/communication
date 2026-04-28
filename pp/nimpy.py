import numpy as np
#a = np.array([0,1,2])

#print(np.mod(a,2))#計算除二的餘數

#print(np.round(123.4444,1))#做浮點數最後面的1，是只取到小數點後第幾位

#print(np.maximum(a,a+2))#在參數中找尋最大值，並呈一個清單

#print(np.ceil([4.2,4.3,6.9]))#無條件進位的意思

#print(np.floor([5.20,4.96,3.01]))#無條件捨去

#print(np.log2(1024))#以二維底取log      

#print(np.sqrt([2,3]))#對每個數開根號

#print(np.sin(np.radians(90)))#將90轉成精度(，再去做sin運算

#print(np.exp([-3,1]))#自然數為底的E，在清單中有負三和一次方

#and 有零就是零
#xor 兩個數不一樣才1
#not 00才是1


#a = np.array([
 #   [1, 2, 3],
  #  [4, 5, 6]
#])
#print(a.sum())

#print(a.sum(axis=0))#值的相加

#print(np.all([0,1,2]))

#print(np.any([False,False,True]))import numpy as np

# 1. 創建模組 (Ch09)
A = np.array([[1, 2], [3, 4]])
B = np.ones((2, 2)) * 5  # 利用純量乘法快速填值

# 2. 統計運算與 Axis (Ch10)
print(f"每欄的總和 (axis=0): {A.sum(axis=0)}") 
print(f"每列的最大值 (axis=1): {A.max(axis=1)}")

# 3. 矩陣轉置與乘法 (Ch10)
# 看看轉置後再做矩陣乘法
C = A.T @ B 

# 4. 廣播機制 (Broadcasting) - 黨員必殺技
# (2, 2) 的矩陣加 (1, 2) 的向量，NumPy 會自動幫你處理！
v = np.array([10, 20])
D = A + v
