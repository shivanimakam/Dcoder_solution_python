n=int(input())
for i in range(n):
    str=input()
    st=str.split()
    if st[1] in st[0]:
        print("Yes")
    else:
        print("No")
