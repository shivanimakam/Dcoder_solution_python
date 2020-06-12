index={}#storing which word comes first in senctence and assign the index
cnt=[]#based on index of dictionary add the count of words
n=int(input())
word_split=list(map(str,input(). split()))
j=0
for i in range(n):
  word=word_split[i]
  if word in index:
    x=index.get(word)
    cnt[x]=cnt[x]+1
  else:
    index[word]=j
    cnt.append(1)
    j=j+1
for i in range(len(cnt)):
  pos=cnt.index(max(cnt))
  for a,b in index.items():
    if b == pos:
        print(a,end=" ")
  cnt[pos]=0
    
  
