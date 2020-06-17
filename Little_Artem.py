test_case=int(input())


for i in range(test_case):
    test="W"
    n,m=[int(i) for i in input().split()]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            else:
                test+="B"

        print(test)
        test=""



