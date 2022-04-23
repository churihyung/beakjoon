n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()
res = [0]*m
for i,x in enumerate(b):
    lt =0
    rt = len(a)-1


    while lt <rt:
        mid = (lt+rt)//2
        if a[mid] > x:
            rt = mid -1
        elif a[mid] < x:
            lt = mid +1
        elif a[mid] == x:
            rt = mid

    print(a[rt])
    for y in a[rt:]:
        if y == x:
            res[i]+=1
        else:
            break

for x in res:
    print(x,end=' ')