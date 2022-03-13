a=[]
while True:
    try:
        n=int(input())
        a.append(n)
    except:
        break
print(max(a))
print(a.index(max(a))+1)