
A=[]
while True:
  str_num = input()
  sum = 0
  if str_num=='0':
    break
  for s in str_num:
    sum += int(s)
  A.append(sum)
for i in A:
  print(i)