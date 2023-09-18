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
        n = int(input())
        s = input()

        arr = [1]
        for i in range(n):
            if s[i]=="<":
                arr.append(arr[i]+1)
            else:
                arr.append(arr[i]-1)

        print(len(set(arr)))

if __name__ == '__main__':
    solve()

#    >><>><>
#    1>0>-1<1>0>-1<1>0

    # 1<2<3>2>1