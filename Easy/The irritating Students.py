n = int(input())
for i in range(n):
  tot=int(input())
  if tot%2 == 0:
    print(int(tot/2),int(tot/2))
  else:
    print(int(tot/2),int((tot/2)+1))
