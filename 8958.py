n = int(input())
for _ in range(n):
    res =0
    a = input()
    p=0
    for x in a:
        if x=='O':
            p+=1
            res+=p
        else:
            p=0
    print(res)
