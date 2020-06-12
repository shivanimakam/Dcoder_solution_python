n=int(input())
m=n
s=0
while(m>0):
  r=m%10
  m=m//10
  s=s+r**3
if s==n:
  print("YES")
else:
  print("NO")
