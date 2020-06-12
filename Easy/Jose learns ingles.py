n=int(input())
letters=list(map(str,input().split()))
sorted_letters=sorted(letters,key=str.casefold)
for i in range(len(sorted_letters)):
    print(sorted_letters[i],end=' ')
