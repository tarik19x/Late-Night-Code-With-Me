tc =int(input())

for _ in range(tc):
    n=int(input())
    a=input()
    if a.count('1') == 0 or a.count('1') == n:
        print(a)
    else:
        start = a.find("1")
        end = a.rfind("0")

        if (start > end):
            print(a)

        else:
            print((start) * "0" + a[end:])

