import math
x,y=list(map(int,input().split()))
for i in range(x,y+ 1):
  flag=0
  for j in range(2, int(math.sqrt(i)+1)):
    if i%j== 0:
      flag=1
      break
  if flag is 0 and i is not 1:
     print(i)
