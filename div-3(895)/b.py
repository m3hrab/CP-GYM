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
        trap_pos = []
        trap_timer = []
        k = INF
        n = read_int()
        for j in range(n):
            d, s = map(int, input().split())
            trap_pos.append(d)
            trap_timer.append(s)

        for i in range(n):
            max_dist = (trap_timer[i]-1)//2
            new_k = trap_pos[i] + max_dist 
            if new_k < k:
                k = new_k

        print(k)
    
if __name__ == '__main__':
    solve()