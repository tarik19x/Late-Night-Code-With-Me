p=int(input())
import string
for i in range(p):
    c=""

    n,a,b=[int(i) for i in input().split()]

    if(n%b==0):
        for j in range(n//b):
            c+=string.ascii_lowercase[:b]

    else:
        for j in range(n//b):
            c+=string.ascii_lowercase[:b]
        c+=string.ascii_lowercase[:n%b]
    print(c)
