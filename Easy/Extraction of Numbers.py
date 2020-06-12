n=int(input())
str=input()
for i in range(len(str)):
    if ord(str[i]) in range(48,58):
        print(str[i],end=" ")
        
