from collections import deque


n = int(input())
cnt=0
for _ in range(n):
    word = input()
    word = deque(word)
    chk=True
    while word:
        if len(word)==1:
            break
        tmp =word.popleft()
        if tmp==word[0]:
            pass
        else:
            if word.count(tmp)>0:
                chk=False
                break
        
    if chk==True:
        cnt+=1

print(cnt)