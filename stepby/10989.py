import sys

a=[0]*10001
n=int(input())

for _ in range(n):
    a[int(sys.stdin.readline())] +=1



for i in range(len(a)):
    if a[i]==0:
        continue
    else:
        for j in range(a[i]):
            print(i)
