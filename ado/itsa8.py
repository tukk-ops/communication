n = int(input())

for i in range(n):
        data = input()
        t= 0
        if len(data) <= 32:
            for char in data:
                    t+=ord(char)
        print(t)
