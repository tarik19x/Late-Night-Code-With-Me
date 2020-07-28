tc =int(input())

for _ in range(tc):
    # n=int(input())
    x,y,n = list(map(int, input().split()))
    a=n%x
    if a==y:
        print(n)
    elif a>y:
        print(n-(a-y))
    else:
        print(n-x+(y-a))