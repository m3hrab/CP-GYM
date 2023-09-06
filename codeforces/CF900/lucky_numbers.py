import sys

INF = float('inf')

# input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))

def max_min(n):
    n = list(str(n))
    m = [int(i) for i in n]
    return max(m), min(m)

def solve():
    for i in range(int(input())):
        l, r = map(int, input().split())

        max_lnmbr = None
        count = float("-inf")
        for i in range(r,l-1,-1):
            mx,mn = max_min(i)
            if (mx-mn)>count:
                count = mx- mn
                max_lnmbr = i 
                if (mx-mn)==9:
                    break 

        print(max_lnmbr)
            

            
if __name__ == '__main__':
    solve()