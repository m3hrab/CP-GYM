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
    n = read_int()
    a = read_ints()
    box = []
    n2 = max(a)
    for i in range(n):
        temp = []
        for j in range(n2):
            temp.append(0)
        box.append(temp)

    for i in range(n):
        for j in range(a[i]):
            box[j][i] = 1
    print(box)
    


# box = max(n)*n
# Fill the box with zero initially
# fill the box with column
    # for i in range(n):
        #for j in range(max(n)):
            #box[max[n-1]-j][i] = 1


if __name__ == '__main__':
    solve()
