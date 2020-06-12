def fact(num):
    if num is 1:
        return 1
    else:
        return num*fact(num-1)
n=int(input())
factval=fact(n)
print(factval)
