N,L=map(int, input().split())
x = {}
for i in range(1, N+1):
    x[i] = int(input())
    if L > x[i]:
        L = L + x[i]//2
    elif L == x[i]:
        L = L + 0
    else:
        L = L // 2
    pass

print(L) 
