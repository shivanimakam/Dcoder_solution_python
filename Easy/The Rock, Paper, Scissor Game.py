n=int(input())
gameval=input()
for i in range(0,len(gameval),2):
  if gameval[i] == gameval[i+1]:
    print("Draw")
  elif gameval[i] =='P' and gameval[i+1] == 'R':
    print("Dcoder")
  elif gameval[i] =='R' and gameval[i+1] == 'P':
    print("You")
  elif gameval[i] =='S' and gameval[i+1] == 'P':
    print("Dcoder")
  elif gameval[i] =='P' and gameval[i+1] == 'S':
    print("You")
  elif gameval[i] =='R' and gameval[i+1] == 'S':
    print("Dcoder")
  elif gameval[i] =='S' and gameval[i+1] == 'R':
    print("You")
    
