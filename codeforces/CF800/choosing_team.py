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
    n, k = map(int, input().split())
    y = read_ints()
    count = 0
    for i in range(n):
        if y[i]+k > 5:
            y[i] = ''
            count += 1 

    while count != 0:
        y.remove('')
        count -= 1

    print(len(y)//3)

if __name__ == '__main__':
    solve()