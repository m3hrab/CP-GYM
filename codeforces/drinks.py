n = int(input())
p = list(map(int, input().split()))
ans = sum(p)*100/(n*100)
print(ans)