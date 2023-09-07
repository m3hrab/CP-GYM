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
        a,b,c = map(int, input().split())

        ans  = 0
        if a != b:
            if a > b:
                mx = a 
                mn = b
            else:
                mx = b
                mn = a

            while mx > mn:
                
                mx -= c
                mn += c 
                ans += 1

        print(ans)



if __name__ == '__main__':
    solve()