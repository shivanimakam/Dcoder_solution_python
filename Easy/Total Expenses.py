n=int(input())
for i in range(n):
    expense=int(input())
    if expense<=1000:
        print("%.2f" %expense)
    else:
        dis=expense*(10/100)
        expense=expense-dis
        print("%.2f" %expense)
        
