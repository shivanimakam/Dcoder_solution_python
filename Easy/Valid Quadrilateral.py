n=int(input())
for i in range(n):
    angles=list(map(int,input().split()))
    if sum(angles) == 360:
        print("YES")
    else:
        print("NO")
