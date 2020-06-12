mark1,mark2,mark3=list(map(int,input().split()))
tot=int((mark1+mark2+mark3)/3)
if tot>90 and tot<=100:
  print("A")
elif tot>80 and tot<=90:
  print("B")
elif tot>70 and tot<=80:
  print("C")
elif tot>60 and tot<=70:
  print("D")
else:
  print("F")
