import sys 
sys.setrecursionlimit(10**6) 

def add_star(x):
    if x ==1:
        return '*'
    else:
        a=[]
        stars = add_star(x//3)
        for i in stars:
            a.append(i*3)
        for i in stars:
            a.append(i+' '*(x//3)+i)
        for i in stars:
            a.append(i*3)

    return a



n = int(input()) 

print('\n'.join(add_star(n)))
