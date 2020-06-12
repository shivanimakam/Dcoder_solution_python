n=int(input())
for i in range(n):
    num=int(input())
    lastdigi=num%10
    firstdigi=int(str(num)[0])
    total=firstdigi+lastdigi
    print(total)
    
