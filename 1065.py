n = int(input())


if(len(str(n))<3):
    print(n)
else:
    cnt=99
    for i in range(100,n+1):
        s = str(i)

        cha1 = int(s[0])-int(s[1])
        cha2 = int(s[1])-int(s[2])

        if cha1==cha2:
            cnt+=1
    print(cnt)
