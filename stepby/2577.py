
t = [0]*42
cnt=0
for _ in range(10):
    t[int(input())%42]+=1
for x in t:
    if x!=0:
        cnt+=1
print(cnt)



