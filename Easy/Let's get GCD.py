#using euclidean algorithm
div= int(input())
divi=int(input())
if divi > div:
  div,divi=divi,div
while(1):
 q=div//divi
 r=div%divi
 if r == 0:
   break
 div=divi
 divi=r
print(divi)
