n = int(input())
for _ in range(n):
    t=''
    a,b = map(str,input().split())
    for x in b:
        t+=x*int(a)
    print(t)
