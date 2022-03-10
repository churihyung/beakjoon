word = list(input())
res = [0]*26
t =list('abcdefghijklmnopqrstuvwxyz')

for x in word:
    x=x.lower()
    res[t.index(x)] +=1
m = max(res)
if res.count(m)>1:
    print('?')
else:
    print(t[res.index(m)].upper())

