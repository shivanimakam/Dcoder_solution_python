n=int(input())
lis=list(map(int,input().split()))
avg=sum(lis)/n
if 2*avg <= 2*int(avg)+1:
  print(int(avg))
else:
  print(int(avg)+1)
