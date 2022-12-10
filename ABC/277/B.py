N= int(input())
arr=[]
judge="Yes"
for i in range(N):
  newStr=list(input())
  if newStr[0]!="H"and newStr[0]!="D" and newStr[0]!="C" and newStr[0]!="S":
    judge="No"
  if newStr[1]!="A"and newStr[1]!="2" and newStr[1]!="3" and newStr[1]!="4"and newStr[1]!="5" and newStr[1]!="6" and newStr[1]!="7"and newStr[1]!="8" and newStr[1]!="9" and newStr[1]!="T"and newStr[1]!="J" and newStr[1]!="K" and newStr[1]!="Q":
    judge="No"
  for i,item in enumerate(arr):
    if newStr == item:
      judge="No"
  arr.append(newStr)

  

print(judge)
