n=int(input())
num=list(map(int,input().split()))
num.sort()
for i in range(len(num)):
  print(num[i],end=' ')
