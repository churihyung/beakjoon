import sys 

def hanoi(n,from_,other,to):
    if n ==1:
        a.append([from_,to])
    else:
        hanoi(n-1,from_,to,other)
        a.append([from_,to])
        hanoi(n-1,other,from_,to)
    return 


a=[]

n = int(input()) 
hanoi(n,1,2,3)

print(len(a))
for x in a:
    print(' '.join(map(str,x)))