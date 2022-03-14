word = input()
cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

for x in cro:
    word = word.replace(x,'*')

print(len(word))
