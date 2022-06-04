from ctypes import alignment
import sys
input = sys.stdin.readline

N = int(input())

print(1)
if N==1:
  exit()
print("1 1")
arr = [1,1]
for i in range(N-2):
  tmp = arr[:]
  arr = [1]
  for k in range(len(tmp)-1):
    arr.append(tmp[k]+tmp[k+1])
  arr.append(1)
  for j in arr:
    if len(arr) == j:
      print(j)
    else:
      print(j,end=" ")
  print()
