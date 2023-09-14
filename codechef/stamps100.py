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
    
def print_array(arr, sep=''):
    print(sep.join(map(str, arr)))


# Main Function
def solve():
    for i in range(read_int()):
        n = read_int()
        s = input()

        for i in range(0,n-2):
            if int(s[i:i+3]) > 100:
                n = s[:i] + '100' + s[i+3:]
                if int(s) > int(n):
                    s = n 
            

        print_array(s)



if __name__ == '__main__':
    solve()
