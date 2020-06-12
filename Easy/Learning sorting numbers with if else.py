m,n,p=list(map(int,input().split()))
if m<n and m<p:
    print(m,end=" ")
    if n>p:
        print(p,end=' ')
        print(n)
    else:
        print(n,end=' ')
        print(p)
elif n<m and n<p:
    print(n,end=" ")
    if m>p:
        print(p,end=' ')
        print(m)
    else:
        print(m,end=' ')
        print(p)
else:
    print(p,end=' ')
    if m>n:
        print(n,end=' ')
        print(m)
    else:
        print(m,end=' ')
        print(n)
