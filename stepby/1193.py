n= int(input())
x=1
while True:
    t = int(x*(x+1)/2)
    tm = int((x+1)*(x+2)/2)
    if x*(x+1)/2<n:
        x+=1
    else:
        break

cnt = int((x*(x+1)/2)-n)

if x%2!=0:
    print(f'{cnt+1}/{x-cnt}')
else:
    print(f'{x-cnt}/{cnt+1}')