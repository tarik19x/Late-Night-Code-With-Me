tc=int(input())
for i in range(tc):
    n=int(input())
    cnt_odd=0
    cnt_even=0
    num=[int(i) for i in input().split()]
    for j in range(len(num)):
        if(j+num[j])%2==0:
            continue
        else:
           if num[j]%2==0:
               cnt_even+=1;
           else:
               cnt_odd+=1
    if(cnt_odd==cnt_even):
        print(cnt_odd)
    else:
        print("-1")