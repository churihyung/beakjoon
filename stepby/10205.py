import math

cnt = int(input())
for _ in range(cnt):
    h,w,n = map(int,input().split())
    y=0
    x=math.ceil(n/h)
    if n%h ==0:
        y=h
    else:
        y=n%h
    print(str(y)+str(x).zfill(2))