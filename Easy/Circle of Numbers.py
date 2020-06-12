n,x=(map(int, input().split()))
h=int(n/2)
x=x+h
if x>=n:
  x=x%n
print(x)


