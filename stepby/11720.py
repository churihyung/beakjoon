word = list(input())
res = [-1]*26
t =list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(word)):
    if res[t.index(word[i])]==-1:
        res[t.index(word[i])] = i

for x in res:
    print(x,end=' ')