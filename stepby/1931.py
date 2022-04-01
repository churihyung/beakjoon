n = int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key = lambda x :(x[1],x[0]))


e_time=0
cnt =0

while True:
    for i,x in enumerate(a):
        if x[0]>=e_time:
            cnt+=1
            e_time=x[1]
            
        
    break

print(cnt)
