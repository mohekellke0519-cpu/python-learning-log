# ここからターミナル入力
n = int(input("nを入力: "))
a = [int(x) for x in input("配列aを入力（空白で区切る）: ").split()]
insertion_sort(a, n)