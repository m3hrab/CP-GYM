import sys

INF = float('inf')

# Fast Input
def read_int():
    return int(sys.stdin.readline())

def read_n_int():
    return map(int, sys.stdin.readline().split())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# Fast output
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    for i in range(int(input())):
        a, b = read_n_int()
        temp = abs(a-b)

        if temp%10 == 0:
            ans = temp//10 
        else:
            ans = temp//10+1

        print(ans)        


if __name__ == '__main__':
    solve()