garry=list(map(int,input().split()))
sharry=list(map(int,input().split()))
Gval=sum(garry)
Sval=sum(sharry)
if Gval > Sval:
  print("Garry",(Gval-Sval))
elif Sval>Gval:
  print("Sharry",(Sval-Gval))
else:
  print("None 0")
