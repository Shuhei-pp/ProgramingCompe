import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  arr.append(input())

count=99999
c_arr = []
for _ in range(0,10):
  c = []
  for i in range(N):
    c.append(arr[i].index(str(_)))
  tmp = Counter(c)
  c_tmp = (max(tmp.values())-1)*10+max(c)
  if(c_tmp < count):
    count = c_tmp

print(count)