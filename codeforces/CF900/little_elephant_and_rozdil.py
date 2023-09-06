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
    towns = read_ints()

    min_distance = INF
    for i in range(n):
        if towns[i] < min_distance:
            min_distance = towns[i]
            indx = i+1
        
    if towns.count(min_distance) > 1:
        print("Still Rozdil")
    else:
        print(indx)


if __name__ == '__main__':
    solve()