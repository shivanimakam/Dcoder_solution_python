n=int(input())
list_num=list(map(str,input().split()))
flag=0
for i in range(0,len(list_num)):
    if list_num[i] is '0':
        flag=1
        break
if flag is 1:
    print("No")
else:
    print("Yes")
