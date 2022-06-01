import sys
import time
input = sys.stdin.readline

N = int(input())

st = time.time()

if N % 2 == 1:
  exit()

def print_b(bit):
  for item in bit:
    if item == "1":
      print("(",end="")
    else:
      print(")",end="")
  print()


for i in  reversed(range(2**N)):
  if i % 2 == 1 or i < 2**(N-1):
    continue
  bit = format(i, f'0{1}b')
  bit = bit.zfill(N)
  sum = 0
  batu = False
  for _,item in enumerate(bit):
    sum += int(item)
    if sum*2 < _+1:
      batu = True
      continue
  if  sum != N/2 or batu:
    continue

  print_b(bit)

# print(time.time()-st)