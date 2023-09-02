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
    for i in range(read_int()):
        n = read_int()
        a = read_ints()
        b = read_ints()

        a.sort()
        b.sort()
        ans = False
        if a==b:
            ans = True
        else:
            for i in range(n):
                if b[i] == a[i]:
                    ans = True
                    continue 
                elif b[i] > a[i]:
                    if a[i] + 1 != b[i]:
                        ans = False 
                        break
                    else:
                        ans = True
                        continue
                    
                else:
                    ans = False
                    break

        print_yes_no(ans)


if __name__ == '__main__':
    solve()