import sys
input = sys.stdin.readline

A = list(map(int, input().split()))

z1=A[0] 
c1=1
for i in A[1:5]:
  if i == z1:
    c1+=1
  else:
    z2=i
if c1 != 3 and c1!=2:
  print('No')
  exit()

c2=0
for i in A[1:5]:
  if i == z2:
    c2+=1

if (c1==2 and c2==3) or (c1==3 and c2==2):
  print("Yes")
  exit()

print("No")
