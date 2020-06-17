t=int(input())

for i in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    b=[]
    if n%2==0:
        for i in range(n//2):
            b.append(a[i])
            b.append(a[n-i-1])

        for i in range(n-1,-1,-1):
            print(b[i],end=" ")
        print()
    else:
        for i in range(n // 2):
            b.append(a[i])
            b.append(a[n - i - 1])

        b.append(a[n//2])

        for i in range(n - 1, -1, -1):
            print(b[i], end=" ")
        print()
