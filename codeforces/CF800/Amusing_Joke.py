import sys

# Define constants
INF = float('inf')
MOD = 10**9 + 7

# Define input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_str():
    return sys.stdin.readline().strip()

def read_strs():
    return list(sys.stdin.readline().split())

# Define output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    guest_name = read_str()
    host_name = read_str()
    pile = read_str()
    card = guest_name + host_name

    flag = False
    temp = list(set(card))
    if len(card) == len(pile):
        for i in range(len(temp)):
            if temp[i] in pile:
                if pile.count(temp[i]) == card.count(temp[i]):
                    flag = True 
                else:
                    flag = False
                    break 
            else:
                flag = False
                break
                
    
    print_yes_no(flag)

if __name__ == '__main__':
    solve()