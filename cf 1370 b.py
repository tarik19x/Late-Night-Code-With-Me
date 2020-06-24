for _ in range(int(input())):
    n = int(input())
    a = [i for i in map(int, input().split(' '))]
    odd = []
    even = []
    len_a=0
    len_b=0

    for i in range(2*n):
        if a[i]%2==0:
            odd.append(i+1)
            len_a+=1
        else:
            even.append(i+1)
            len_b+=1

    if(len_a%2==0):
        if(len_a>=2):
            odd.pop()
            odd.pop()
        else:
            even.pop()
            even.pop()
    else:
        odd.pop()
        even.pop()

    even+=odd

    for i in range(0,len(even)-1,2):
        print(even[i]," ",even[i+1])

