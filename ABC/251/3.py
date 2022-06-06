import sys
input = sys.stdin.readline

n =int(input())
top = 0
name_list = set()
index = 0
for i in range(n):
  name,p= input().split()
  if not name in name_list:
    name_list.add(name)
  else:
    continue
  if int(p) <= top:
    continue
  top = int(p)
  index = i+1
print(index)
