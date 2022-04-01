n = int(input())

a=list(map(int,input().split()))
a.sort()
m = int(input())
b=list(map(int,input().split()))




for x in b:
    st=0
    ed=n-1
    mid=(st+ed)//2
    while True:
        if st > ed:
            print(0)
            break
        if x==a[mid]:
            print(1)
            break
        elif x>a[mid]:
            st=mid+1
            mid=(st+ed)//2
        elif x<a[mid]:
            ed=mid-1
            mid=(st+ed)//2
        