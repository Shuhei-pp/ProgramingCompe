import sys
from collections import Counter 
input = sys.stdin.readline
A=[]
for i in sys.stdin.read():
  str_low = i.lower()
  A.append(str_low)

str_c_list = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in A:
  str_c_list.append(Counter(i))
for _ in alphabet:
  count= 0
  for i in str_c_list:
    count += i[_]
  print(_+" :",end=" ") 
  print(count)
