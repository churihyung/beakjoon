n = input()

chk = [[],[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L']
,['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
res=0
for x in n:
    for z in chk:
        if x in z:
            res += chk.index(z)
print(res)