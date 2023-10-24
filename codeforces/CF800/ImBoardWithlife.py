from functools import cache

@cache
def fact(n):
    # Note1: getting error because of RecursionError 
    # Note2: Python has a default maximum recursion depth of 1000 
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    # total = 1 
    # for i in range(1,n+1):
    #     total *= i 
    
    # return total



a, b = map(int, input().split())

ans = fact(min(a,b))
print(ans)