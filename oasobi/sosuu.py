n = int(input("2以上の数字を入力してね:"))
import time

start = time.time()

for i in range(2,n+1):
  for j in range(2,int(i**(0.5)+1)):
    if float.is_integer(i/j):
      break
  else: #breakしなかったら
    print(i)

print("使用時間:"+str(time.time()-start))
