a_list,b_list = [],[]
while True:
  a,b = map(int, input().split())
  if a == 0 and b== 0:
    break
  a_list.append(a)
  b_list.append(b)

for i,item in enumerate(a_list):
  for j in range(item):
    for k in range(b_list[i]):
      print('#',end='')
    print()
  print()