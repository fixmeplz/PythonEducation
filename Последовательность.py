n=int(input())
k=0
L=[]
for i in range(n+1):
  if len(L)==n:
    break
  for j in range(i):
    L.insert(k, str(i))
    k+=1
    if len(L)==n:
     break
print(*L)