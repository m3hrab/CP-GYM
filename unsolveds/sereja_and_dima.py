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
    cards = read_ints()
    cards.sort(reverse=True)
    sereja = 0
    dima = 0
    print(cards)
    for i in range(n):
        if i%2==0:
            sereja += cards[i]
        else:
            dima += cards[i]

    print("%d %d"%(sereja,dima))
    
if __name__ == '__main__':
    solve()

[48, , 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 33, 32, 31, 29, 28, 27, 26, 25, 24, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 7, 6, 5, 4, 3, 1]