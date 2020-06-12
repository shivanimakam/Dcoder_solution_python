n=int(input())
words=list(map(str,input().split()))
index=words.index('Nemo')
if index is -1:
    print("-1")
else:
    print(index+1)
