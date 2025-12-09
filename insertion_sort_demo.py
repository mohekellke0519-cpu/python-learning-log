# ファイル名: insertion_sort_demo.py

def print_array(a):
    """配列を1行で表示"""
    print(*a)

def insertion_sort(a, n):
    """挿入ソートの過程を表示"""
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        print_array(a)

# --- ターミナル入力 ---
n = int(input("配列の要素数 n を入力してください: "))
a = [int(x) for x in input(f"{n} 個の整数を空白で区切って入力してください: ").split()]

# 入力数が n と合っているかチェック
if len(a) != n:
    print(f"入力された要素数が n={n} と一致しません。終了します。")
else:
    print("ソートの過程:")
    insertion_sort(a, n)
    print("ソート完了後の配列:")
    print_array(a)
