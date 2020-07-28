import math
tc =int(input())

for _ in range(tc):
    a,b=arr=list(map(int,input().split()))
    min_=min(a,b)
    max_=max(a,b)
    if(max_>2*min_):
        print(int(max_*max_))
    else:
        print(int(math.pow(min_*2,2)))
