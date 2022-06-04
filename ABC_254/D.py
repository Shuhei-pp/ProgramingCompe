import sys
import math
import time
input = sys.stdin.readline

N = int(input())

st = time.time()
count=0

max_sq = int(math.sqrt(N))
sum = 0
for i in range(max_sq+1):
  sum += i
print(sum + N -1)
# for j in range(1,N+1):
#   for k in range(1,N+1):

#     if math.sqrt(j*k)%1 == 0:
#       count += 1
# print(count)
# print(time.time()-st)