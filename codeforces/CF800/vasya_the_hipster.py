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


def solve():
    a, b = map(int, input().split())
    total = (a+b)//2
    different = min(a,b)
    same = (total-different)

    print("%d %d"%(different, same))
    

if __name__ == '__main__':
    solve()