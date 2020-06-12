maxW=int(input())
value1,weight1=list(map(int,input().split()))
value2,weight2=list(map(int,input().split()))
if weight1+weight2<=maxW:
  total=value1+value2
elif value1>=value2 and maxW>=weight1:
  total=value1
elif maxW>=weight2:
  total=value2
else:
  total=0
print(total) 
