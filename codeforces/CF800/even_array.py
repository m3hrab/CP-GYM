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
from math import gcd, sqrt

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
        n = read_int()
        a = read_ints()
        even = 0
        odd = 0

        for number in a:
            if number%2==0:
                even += 1
            else:
                odd += 1

        if n%2 == 0:
            if even != odd:
                print("-1")
                continue 
        else:
            if even != odd+1:
                print("-1")
                continue 
        

        count = 0
        
        for i in range(n):
            if i%2 == 0:
                if a[i]%2 == 1:
                    for j in range(i+1,n):
                        if j%2==1:
                            if a[j]%2==0:
                                a[i],a[j] = a[j],a[i]
                                count += 1
                                break 

            else:
                if a[i]%2==0:
                    for j in range(i+1,n):
                        if j%2==0:
                            if a[j]%2==1:
                                a[i],a[j] = a[j],a[i]
                                count += 1
                                break 
                            
        print(count)

            
if __name__ == '__main__':
    solve()
