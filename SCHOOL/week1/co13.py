command = input().strip()

# 轉置矩陣 (TRANSPOSE)
if command == "TRANSPOSE":
    r, c = map(int, input().split())
    matrix = []
    for _ in range(r):
        matrix.append(list(map(int, input().split())))
    
    # 建立一個 c 橫 r 直的新矩陣
    for j in range(c):
        row_result = []
        for i in range(r):
            row_result.append(matrix[i][j])
        print(*row_result)

# 矩陣相加 (ADD) 與 相乘 (MUL)
elif command == "ADD" or command == "MUL":
    # 讀取第一個矩陣
    r1, c1 = map(int, input().split())
    matrix_a = []
    for _ in range(r1):
        matrix_a.append(list(map(int, input().split())))
        
    # 讀取第二個矩陣
    r2, c2 = map(int, input().split())
    matrix_b = []
    for _ in range(r2):
        matrix_b.append(list(map(int, input().split())))
        
    if command == "ADD":
        # 相加條件：維度必須完全相同
        if r1 == r2 and c1 == c2:
            for i in range(r1):
                row_result = []
                for j in range(c1):
                    row_result.append(matrix_a[i][j] + matrix_b[i][j])
                print(*row_result)
        else:
            print("Invalid input")
            
    elif command == "MUL":
        # 相乘條件：第一個矩陣的行數 (c1) 等於第二個矩陣的列數 (r2)
        if c1 == r2:
            for i in range(r1):
                row_result = []
                for j in range(c2):
                    # 計算內積
                    dot_product = 0
                    for k in range(c1):
                        dot_product += matrix_a[i][k] * matrix_b[k][j]
                    row_result.append(dot_product)
                print(*row_result)
        else:
            print("Invalid input")

# 指令錯誤
else:
    print("Invalid input")