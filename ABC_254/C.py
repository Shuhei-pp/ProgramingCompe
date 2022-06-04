import sys
input = sys.stdin.readline

N,K = map(int, input().split())
A = list(map(int, input().split()))

A_s=A[:]
A_s.sort()
if A == A_s:
  print("Yes")
  exit()

A_t = A[:]
for _ in range(K):
  tmp = A_t[_::K]
  tmp.sort()
  for i,item in enumerate(tmp):
    A_t[_+i*K] = item
  if A_s == A_t:
    print("Yes")
    exit()
  if A_s[0:_] != A_t[0:_]:
    break
print("No")

  

