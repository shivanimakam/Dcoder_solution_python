n=int(input())
for i in range(n):
  year=int(input()) 
  if year%400 is 0 or year%4 is 0 and year%100!=0:
    print("Yes") 
  else:
    print("No")
