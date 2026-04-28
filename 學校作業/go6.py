n = int(input())
dd = []
for _ in range(n):
    start, end = map(int, input().split())
    dd.append((start, end))
dd.sort()
conflict = False

for i in range(1,len(dd)):
    now = dd [i][0]
    last = dd [i-1][1]
    if now < last:
        conflict =True
        break

if conflict:
    print("Conflict found")
else:
    print("Schedule OK")