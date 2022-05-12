import sys
list_a = []
list_b = []
count = 0
while True:
  try:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
      break
    list_a.append(a)
    list_b.append(b)
    count += 1
  except EOFError:
    break
for i in range(count):
  if list_b[i] < list_a[i]:
    print(list_b[i],list_a[i])
  else:
    print(list_a[i],list_b[i])

