n= int(input())
s=set()
for _ in range(n):
    t=input()
    s.add((t,len(t)))
s=list(s)
s= sorted(s, key = lambda x : (x[1], x[0]))

for x in s:
    print(x[0])