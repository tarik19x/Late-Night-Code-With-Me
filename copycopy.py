test_case=int(input())
for i in range(test_case):
    n=input()
    s=set([int(i) for i in input().split()])
    print(len(s))