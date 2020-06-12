str1=input()
str2=""
for i in range(len(str1)):
  if str1[i] in str2:
    str2=str2
  else:
    str2=str2+str1[i]
print(str2)
