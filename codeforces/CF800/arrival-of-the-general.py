n = int(input())
a = list(map(int, input().split()))
max_n = a[0]
min_n = a[0]
max_ind = 0
min_ind = 0
for i in range(n):
    if a[i] <= min_n:
        min_n = a[i]
        min_ind = i 

    if a[i] > max_n:
        max_n = a[i] 
        max_ind = i

n = n - 1
if max_ind < min_ind:
    ans = max_ind + (n - min_ind)

else:
    ans = max_ind + (n-min_ind) - 1

print(ans)

n = int(input())
a = list(map(int, input().split()))
max_n = a[0]
min_n = a[0]
max_ind = 0
min_ind = 0
for i in range(n):
    if a[i] <= min_n:
        min_n = a[i]
        min_ind = i 

    if a[i] > max_n:
        max_n = a[i] 
        max_ind = i

n = n - 1
if max_ind < min_ind:
    ans = max_ind + (n - min_ind)

else:
    ans = max_ind + (n-min_ind) - 1

print(ans)

