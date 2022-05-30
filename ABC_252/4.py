import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N-1):
  for j in range(i+1,N-1):
    B = A[:]
    del B[i],B[j]
    B = [s for s in B if s != A[i]]
    B = [s for s in B if s != A[j]]
    count += len(B)

print(count)
