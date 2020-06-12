n=int(input())
for i in range(n):
    math,algo=list(map(int,input().split()))
    if math > 70 and algo > 50:
        print("Pass")
    else:
        print("Fail")
