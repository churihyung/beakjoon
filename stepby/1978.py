import math
n = input()
a = list(map(int,input().split()))

def prime(n):
    cnt=0
    if n==1: return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x ==0:
            return False
    else: return True
cnt=0
for x in a:
    
    if prime(x):
        cnt+=1

print(cnt)