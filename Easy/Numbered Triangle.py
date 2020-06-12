n=int(input())
for i in range(1,n+1):
    for j in range (1,i+1):
        if j is i:
            print(j)
        else:
            print(j,end=' ')
