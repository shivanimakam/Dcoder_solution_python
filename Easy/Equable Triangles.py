import math
n = int(input())
for i in range(n):
  a,b,c=list(map(int, input().split()))
  sum=a+b+c
  p=sum/2
  area=math.sqrt(p*(p-a)*(p-b)*(p-c))
  if sum == area:
    print("True")
  else:
    print("False")
