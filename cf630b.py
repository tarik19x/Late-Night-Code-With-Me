prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for ii in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    ind = 0
    flag = [0] * 13
    c = 0
    for i in range(n):
        for j in range(len(prime)):
            if arr[i] % prime[j] == 0:

                if(flag[j]==0):
                    ind+=1
                    flag[j]=ind
                    ans.append(ind)
                else:
                    ans.append(flag[j])
                break


    print(ind)
    print(*ans)