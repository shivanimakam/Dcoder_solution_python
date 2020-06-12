n=int(input())
integers=list(map(int,input().split()))
#considering list starts from index 0 and finding even numbers at odd index
for i in range(1,n,2):#starting index from 1 to find even numbers at odd index
    if integers[i]%2 is 0:
        print(integers[i],end=' ')
    
