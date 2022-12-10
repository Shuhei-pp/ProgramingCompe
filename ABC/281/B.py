S = input()

if len(S)!=8:
  print("No")
  exit()

if not str.isalpha(S[0]):
  print("No")
  exit()
if not str.isalpha(S[7]):
  print("No")
  exit()
for i in range(1,7):
  if not str.isdecimal(S[i]):
    print("No")
    exit()
  
if not 100000 <= int(S[1:7]) <= 999999:
  print("No")
  exit()


print("Yes")

