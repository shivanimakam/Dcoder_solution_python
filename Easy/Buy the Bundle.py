n=int(input())
for i in range(n):
  ns,bv=list(map(int, input().split()))
  if bv%ns==0:
    print("Yes")
  else:
    print("No")
