N=int(input())

l,r = map(int,input().split())
larr=[l]
rarr=[r]

for i in range(N-1):
  l,r = map(int,input().split())
  L1=0
  lll=len(larr)
  R1=lll
  
  while R1-L1>1:
    mid=(R1+L1)//2
    if larr[mid]<l:
      L1=mid
    else:
      R1=mid
  if l > larr[L1]:
    L1+=1

  L2=0
  R2=lll
  
  while R2-L2>1:
    mid=(R2+L2)//2
    if rarr[mid]<r:
      L2=mid
    else:
      R2=mid

  if r > rarr[L2]:
    L2+=1

  if L1 != 0:
    if rarr[L1-1]>=l:
      L1-=1
      l=larr[L1]

  if L2 != lll:
    if larr[L2]<=r:
      r=rarr[L2]
      L2+=1

  larr[L1:L2]=[l]
  rarr[L1:L2]=[r]

for i,item in enumerate(larr):
  print(item,rarr[i])
