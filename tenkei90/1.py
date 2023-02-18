import sys
input = sys.stdin.readline

N,L=  map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# nibu
def judge(x):
  parts = 0
  count = 0
  for i,item in enumerate(A):
    it = item - parts
    if it >= x:# xよりでかい長さで切れ込みを入れることができた場合
      parts += it
      count += 1
      if count == K:
        if L - parts >= x:
          return True
  return False

left = 0
right = L
while right - left > 1:
  mid = int((right + left)/2)
  print(mid)
  if judge(mid) == True:
    left = mid
  else:
    right = mid
print(left)
