num=int(input())
if num >=0:
  for i in range(num+1):
    if i !=num:
      print(2**i,end=',')
    else:
      print(2**i)
else:
  numx=-1
  print("1.0",end=',')
  while(numx!=num):
    if numx!=num:
      print(2**numx,end=',')
      numx=numx-1
  else:
    print(2**numx)            
      
    
  
