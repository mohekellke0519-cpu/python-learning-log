s=input().strip()
a=int(input().strip())
i = [input().strip() for _ in range(a)]
for t in i:
    if s in t:
        print("Yes")
    else:
        print("No")
    
