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

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
    
def solve():
    n = read_int()
    m = 4

    while True:
        if is_prime(m):
            m += 1
            continue
        else:
            temp = n - m 
            if is_prime(temp):
                m += 1
                continue 
            else:
                print("%d %d"%(m,temp))
                break 

        m += 1    

if __name__ == '__main__':
    solve()