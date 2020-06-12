str=input()
str=str.lower();
unique=set()
for i in range(len(str)):
    unique.add(str[i])
if len(unique) is 26:
    print("YES")
else:
    print("NO")
