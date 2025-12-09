N,K =map(int, input().split())
#N:カードのサイズ, K:引かれる数字の数
card = [list(map(int, input().split())) for _ in range(N)]
#listでまとめるときは内包表記を使うと便利
draws = set(map(int, input().split()))
#setは同じ数が出ても1度だけ格納される
opened = [[(i == N//2 and j == N//2) or card[i][j] in draws for j in range(N)] for i in range(N)]
# ==N//2 は真ん中のマスを開けるための条件式
# 内側のリストは for j in range(N), 外側のリストは for i in range(N)
#card[i][j]がdrawsに含まれているかを判定してTrue/Falseを格納
bingo = 0
#初期値0に設定
for i in range(N):
    if all(opened[i][j] for j in range(N)):
        #行方向のビンゴ判定 i行目の全てのマスがTrueか判定
        bingo += 1
    if all(opened[j][i] for j in range(N)):
        #列方向のビンゴ判定 j列目の全てのマスがTrueか判定
        bingo += 1
if all(opened[i][i] for i in range(N)):
        bingo += 1 
        #右下がりの斜めビンゴ判定 1回しかカウントしないため方向のループから外す
if all(opened[i][N-1-i] for i in range(N)):
        bingo += 1
        #左下がりの斜めビンゴ判定 1回しかカウントしないため方向のループから外す

print(bingo)