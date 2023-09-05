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
    for i in range(int(input())):
        l = read_ints()
        count = 0
        for i in range(1,4):
            if l[i] > l[0]:
                count += 1

        print(count)
if __name__ == '__main__':
    solve()