tc=int(input())
for _ in range(tc):
    flag=False
    n,m = list(map(int, input().split()))
    arr_n=list(map(int, input().split()))
    arr_m=list(map(int, input().split()))
    a_set = set(arr_n)
    b_set = set(arr_m)

    if (a_set & b_set):
        print("YES")
        c=a_set & b_set
        print("1 ",c.pop())
    else:
        print("NO")


