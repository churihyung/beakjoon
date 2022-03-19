a,b = map(int,input().split())
cards = list(map(int,input().split()))
min = 2147000000
res = 0
for x in range(len(cards)-2):
    fir = cards[x]
    for y in range(x+1,len(cards)-1):
        sec = cards[y]
        for z in range(y+1,len(cards)):
            rd = cards[z]
            cha = b-(fir+sec+rd)
            if cha <0:
                continue
            else:
                if min > cha:
                    min = cha
                    res = fir+sec+rd

print(res)