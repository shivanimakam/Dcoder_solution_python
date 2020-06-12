import math
n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in range(len(li)):
    flag=0
    for j in range(2,int(math.sqrt(li[i])+1)):
        if li[i]%j==0:
            flag=1
            break
    if flag is 0 and li[i]!=1:
        cnt=cnt+1
print(cnt)
