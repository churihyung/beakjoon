import math
a = int(input())
b = int(input())
prime_num = []
def prime(n):
    cnt=0
    if n==1: return False
    for x in range(2, int(math.sqrt(n))+1):
        if n % x ==0:
            return False
    else: return True
cnt=0
for x in range(a,b+1):
    
    if prime(x):
        prime_num.append(x)

if len(prime_num) ==0:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))