n=int(input())
list1=list(map(int,input().split()))
list1=sorted(list1, reverse=True)
for i in range(len(list1)):
  print(list1[i],end=' ')
