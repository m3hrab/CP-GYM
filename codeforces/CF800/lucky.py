"""

/  \     /  |          /  |                         /  |      
$$  \   /$$ |  ______  $$ |____    ______   ______  $$ |____  
$$$  \ /$$$ | /      \ $$      \  /      \ /      \ $$      \ 
$$$$  /$$$$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$$  |
$$ $$ $$/$$ |$$    $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ |  $$ |
$$ |$$$/ $$ |$$$$$$$$/ $$ |  $$ |$$ |     /$$$$$$$ |$$ |__$$ |
$$ | $/  $$ |$$       |$$ |  $$ |$$ |     $$    $$ |$$    $$/ 
$$/      $$/  $$$$$$$/ $$/   $$/ $$/       $$$$$$$/ $$$$$$$/ 
                                    

"""


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
    for i in range(read_int()):
        n = list(input())
        for i in range(len(n)):
            n[i] = int(n[i])

        ans = False 
        if sum(n[:3]) == sum(n[3:]):
            ans = True 

        print_yes_no(ans)

if __name__ == '__main__':
    solve()
