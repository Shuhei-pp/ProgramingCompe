n = int(input())
i = 1
while True:
  x = i
  if x % 3 == 0:
    print(" "+str(i),end="")
    x = False
  while x:
    if x % 10 == 3:
      print(" "+str(i),end="")
      break
    x = int(x/10)
  i += 1
  if i > n:
    break
print()
