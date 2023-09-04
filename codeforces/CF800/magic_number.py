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
    n = list(input())
    t = len(n)
    for i in range(t-2):
        if n[i]=='1' and n[i+1]=='4' and n[i+2]=='4':
            n[i],n[i+1],n[i+2] = '','',''

    for i in range(t-1):
        if n[i]=='1' and n[i+1]=='4':
            n[i],n[i+1] = '',''

    for i in range(t):
        if n[i]=='1':
            n[i] = ''

    while n.count('') != 0:
        n.remove('')

    if len(n) == 0:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    solve()