a,b=list(map(int,input().split()))
sum=a+b
if a == 11 or b == 11:
    sum=sum-10
    print(sum)
elif sum>21:
    print("0")
else:
    print(sum)
    
