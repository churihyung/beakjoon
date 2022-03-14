import math

n = int(input())
a=1
while True:
    if n==1:
        break
    else:
        if 3*(a-1)**2+3*(a-1)+1>=n:
            break
        else:
            a+=1
print(a)