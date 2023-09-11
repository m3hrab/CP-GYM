import sys

# Constants
INF = float('inf')
MOD = 1000000007

# Faster Input
def read_int():
    return int(sys.stdin.readline())

def read_n_int():
    return map(int, sys.stdin.readline().split())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))


# Faster Output
def print_yes_no(condition):
    print('YES' if condition else 'NO')
    
def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


# Main Function
def solve():
    n = read_int()
    cards = read_ints()
    sereja = []
    dima = []
    flag = True
    while len(cards) != 0:
        if cards[0] > cards[-1]:
            temp = cards[0]
            cards.pop(0)
        else:
            temp = cards[-1]
            cards.pop(-1)

        if flag:
            sereja.append(temp)
            flag = False 
        else:
            dima.append(temp)
            flag = True 

    print("%d %d"%(sum(sereja), sum(dima)))

if __name__ == '__main__':
    solve()
