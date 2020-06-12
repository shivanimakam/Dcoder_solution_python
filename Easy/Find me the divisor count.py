l,h,d=list(map(int,input().split()))
cnt=0
for i in range(l,h+1):
  if i %d==0:
    cnt=cnt+1
print(cnt)
    
