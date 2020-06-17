

for i in range(int(input())):
   n = int(input())
   s = list(map(int, input().split()))
   ok = False
   for i in range(n-2):
       for j in range(i + 2, n):
           if s[i] == s[j]:
               ok=True
               break

   print('YES' if ok else 'NO')
    