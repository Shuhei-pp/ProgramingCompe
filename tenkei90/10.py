import sys
input = sys.stdin.readline

N= int(input())

A=[0 for i in range(N+1)]
B=[0 for i in range(N+1)]
A[0] = 0
B[0] = 0
c,p = map(int, input().split())
if c == 1:
  A[1] = p
else:
  B[1] = p
for i in range(N-1):
  c,p = map(int, input().split())
  if c == 1:
    A[i+2] = A[i+1]+p
    B[i+2] = B[i+1]
  else:
    A[i+2] = A[i+1]
    B[i+2] = B[i+1]+p

Q = int(input())

for i in range(Q):
  left,right = map(int, input().split())
  print(A[right]-A[left-1],B[right]-B[left-1])


