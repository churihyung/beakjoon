from collections import deque


n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    a = deque(a)
    m = a.popleft()
    s = sum(a)
    avg_ = round(s/m,4)
    up = 0
    for i in a:
        if i>avg_:
            up+=1
    print("{:.3f}%".format(up/m*100))

