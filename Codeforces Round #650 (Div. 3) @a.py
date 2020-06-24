from collections import OrderedDict
tc=int(input())

for i in range(tc):
    a=input()
    my_list=""
    for j in range(0,len(a),2):
        my_list+=((a[j]))
    my_list+=(a[len(a)-1])
    print(my_list)

