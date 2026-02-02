N,M = map(int,input().split())
x= [int(input()) for _ in range(N-1)]
jam = 0
total = 0
for a in x:
    if a <=M:
        jam += a 
    else:
        total += jam
        jam = 0

total += jam

print(total)