def print_array(a):
    print(*a)

def insertion_sort(a, n):
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j >= 0 and x < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
        print_array(a)

# ここからターミナル入力
n = int(input("nを入力: "))
a = [int(x) for x in input("配列aを入力（空白で区切る）: ").split()]
insertion_sort(a, n)