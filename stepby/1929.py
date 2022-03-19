import math
a,b = map(int,input().split())
prime_num = []
def prime(n):
    if n==1: return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x ==0:
            return False
    else: return True
cnt=0
for x in range(a,b+1):
    
    if prime(x):
        prime_num.append(x)

for x in prime_num:
    print(x)