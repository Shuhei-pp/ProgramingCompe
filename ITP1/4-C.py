import math
a_list = []
op_list = []
b_list = []
while True:
  column = list(input().split())
  if column[1] == "?":
    break
  a_list.append(int(column[0]))
  op_list.append(column[1])
  b_list.append(int(column[2]))
for i,item in enumerate(op_list):
  if item == "+" :
    print(a_list[i]+b_list[i])
  elif item == "-":
    print(a_list[i]-b_list[i])
  elif item == "*":
    print(a_list[i]*b_list[i])
  elif item == "/":
    print(math.floor(a_list[i]/b_list[i]))
