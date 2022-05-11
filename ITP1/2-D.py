w,h,x,y,r = map(int, input().split())
if w >= x and h >= y and x >= 0 and y>= 0:# 四角内に中心点が有るかどうか
  if (w - x) >= r and x >= r:#円書いてどうか
    if (h - y) >= r and y >= r:  
      print("Yes")
      exit()
print("No")

