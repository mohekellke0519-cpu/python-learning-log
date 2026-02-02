n = int(input())
# n: マスの数
w = list(map(int,input().split())) 
# w: 各マスの状態を表すリスト (0: 雨, 1: 曇, 2: 晴)
nj = []
for i in range(1,n):
    #   1 から n-1 までループ
    if w[i-1] == 2 and w[i]== 0 :
        # 晴れから雨に変わるマスの番号を記録
        nj.append(i)
            # i は 1-indexed にするため 
if nj:
    print(*nj)
else:
    print(-1)