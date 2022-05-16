import sys
input = sys.stdin.readline

N,K =  map(int, input().split())
S = list(input())

c_str = []
tmp = []
for _,it in enumerate(S):
  if not it in tmp:
    tmp.append(it)
  else:
    c_str.append(tmp)
    tmp = []
    tmp.append(it)
tmp.pop()
c_str.append(tmp)
print (c_str)
  
  

