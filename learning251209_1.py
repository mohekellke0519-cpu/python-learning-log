print("egg")

print("sky")

#D問題
n = int(input())
p = int(input())

cost = n * p

print(cost)

#C問題
N,X,Y=map(int, input().split())
#複数の値を入れたいときはmapを使う
for i in range(1,N+1):
#iは1からNまで
    if i % X ==0 and i % Y==0:
        print("AB")
    elif i % X ==0:
        print("A")
    elif i % Y ==0:
        print("B")
    else:
        print("N")
    
