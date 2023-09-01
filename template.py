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
    day = 1
    total_finish = 0
        
    while True:
        total_finish += reads_count[day-1]
        if total_finish >= n:
            break
        day += 1
        if day > 7:
            day = 1
    
    print(day)

if __name__ == '__main__':
    solve()