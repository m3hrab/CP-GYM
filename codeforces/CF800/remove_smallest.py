import sys

# Define constants
INF = float('inf')
MOD = 10**9 + 7

# Define input functions
def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

# Define Output functions
def print_yes_no(condition):
    print('YES' if condition else 'NO')

def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))


def solve():
    for i in range(read_int()):
        n = read_int()
        a = read_ints()
        
        if n>1:
            for i in range(n):
                swaped = False
                for j in range(n-i-1):
                    if a[j]>a[j+1]:
                        a[j], a[j+1] = a[j+1], a[j]
                        swaped = True 
                
                if swaped == False:
                    break
            
            flag = True
            for i in range(n-1):
                if abs(a[i]-a[i+1]) > 1:
                    flag = False
                    break 

            print_yes_no(flag)
        
        else:
            print("YES")
        

if __name__ == '__main__':
    solve()