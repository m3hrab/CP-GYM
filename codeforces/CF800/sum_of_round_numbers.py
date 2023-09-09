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
    for i in range(int(input())):
        n = int(input())
        temp = []
        power = 1
        while n>0:
            m = n%10
            if m > 0:
                temp.append(m*power)
            
            n = n//10
            power *= 10
        
        print(len(temp))
        print_array(temp)
        
        


if __name__ == '__main__':
    solve()