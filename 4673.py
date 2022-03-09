t=[]
for i in range(30001):
    t.append(i)

for i in range(1,10001):
    if i ==0:
        continue
    chk=i
    n = str(i)
    for x in n:
        chk+=int(x)
    t[chk]=0

for x in t:
    if x>0 and x <=10000:
        print(x,end=' ')

