n=int(input())
for i in range(n):
    size=int(input())
    num=list(map(int,input().split()))
    num=sorted(num,reverse=True)
    for j in range(len(num)):
        print(num[j],end='')
    print()
