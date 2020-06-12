import math
num=abs(int(input()))
flag=0
for i in range(2,abs(int(math.sqrt(num)+1))):
  if abs(num/i==i) and abs(num%i==0):
    flag=1
    break
if flag==0:
  print("NO")
else:
  print("YES")
