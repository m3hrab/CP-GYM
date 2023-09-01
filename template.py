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
    n = read_int()
    reads_count = read_ints()
    day = 0
    total_finish = 0
    if sum(reads_count)*2 <= n:
        n = n - sum(reads_count)

    while total_finish < n:
        total_finish += reads_count[day]
        day += 1
        if day > 6:
            day = 1
    
    print(day)

if __name__ == '__main__':
    solve()