str1=input()
str1=str1.lower()
cnt=0
for i in range(len(str1)):
  if str1[i] == 'a' or  str1[i] == 'e' or str1[i] =='i' or str1[i] =='o' or str1[i] =='u':
    cnt=cnt+1
print(cnt)
