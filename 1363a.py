tc =int(input())

for _ in range(tc):
    n,x=arr=list(map(int,input().split()))
    l=list(map(int,input().split()))
    odd = 0
    for a in l:
        if a % 2 == 1:
            odd += 1
    if odd == 0 or (odd == n and x % 2 == 0) or (x == n and odd % 2 == 0):
        print("NO")
    else:
        print("YES")