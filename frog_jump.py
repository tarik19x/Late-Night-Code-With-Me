n=int(input())

for i in range(n):
    cnt=1
    max_cnt=1
    pre_s=input()
    s="R"+pre_s+"R"


    for i in s:
        if i=='L':
            cnt+=1
            max_cnt=max(max_cnt,cnt)
        if i=='R':
            cnt=1

    print(max_cnt)





