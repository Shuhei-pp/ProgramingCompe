import sys
input = sys.stdin.readline

N = int(input())
S = input()

l_s=list(S)
if N == 2:
  if l_s[0] == l_s[1]:
    print('Yes')
  else:
    print('No')
  exit()

if l_s[0] == "B" or l_s[N-1] == "A":
  print('Yes')
  exit()

print('No')





