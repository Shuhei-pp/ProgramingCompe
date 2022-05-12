a,b,c = map(int, input().split())
count = 0
for i in range(1,c+1):
  if c % i == 0:
    if i > b:
      break
    if a <= i and i <= b:
      count += 1
print(count)
