list = []
list.append()
ではなく
list = set()
list.add()
めっちゃ早い。inも早くなる。

input = sys.stdin.readline
を使う。特に読み込み多いやつは必須。

sorted()よりsort()の方が早い。

for i in ~
より
for _ in ~。

二次元配列作成
[[0]*n for _ in range(n)]
が早い
