import sys
from time import time
input = sys.stdin.readline

H,W = map(int, input().split())
square = []

square= [list(map(int, input().split())) for i in range(H)]
st= time()

sum_r=[]
for row in square:
  sum_r.append(sum(row))

sum_c=[]
for c in range(W):
  sum_c.append(sum([r[c]for r in square]))

for r,row in enumerate(square):
  print(*[sum_r[r] + sum_c[c] - item for c,item in enumerate(row)])
# print(time() -st)
