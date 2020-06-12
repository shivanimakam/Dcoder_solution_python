n=int(input())
str1=input()
x,y=list(map(int,input().split()))
if str1[x].islower():
  xval=str1[x].upper()
else:
  xval=str1[x].lower()
if str1[y].islower():
  yval=str1[y].upper()
else:
  yval=str1[y].lower()
str1=str1[0:x]+xval+str1[x+1:y]+yval+str1[y+1:]
print(str1)


