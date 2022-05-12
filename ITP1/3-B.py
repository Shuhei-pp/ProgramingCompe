import sys
a = []
for l in sys.stdin:
  a.append(int(l))
for i,item in enumerate(a):
  if item == 0:
    exit() 
  print("Case "+str(i+1)+": "+str(item))