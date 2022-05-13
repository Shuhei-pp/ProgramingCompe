a_list,b_list = [],[]
while True:
  a,b = map(int, input().split())
  if a == 0 and b== 0:
    break
  a_list.append(a)
  b_list.append(b)

for i,item in enumerate(a_list):
  for k in range(b_list[i]):
    print('#',end='')
  print()
  for j in range(item-2):
    print('#',end='')
    for k in range(b_list[i]-2):
      print('.',end='')
    print('#')
  for k in range(b_list[i]):
    print('#',end='')
  print('\n')