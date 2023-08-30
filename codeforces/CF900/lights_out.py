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
    switches = []
    for i in range(3):
        switches.append(read_ints())

    lights = [[1]*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            switch = switches[i][j]
            if switch%2 == 1:
                if lights[i][j] == 1:
                    lights[i][j] = 0
                else:
                    lights[i][j] = 1

                # check top, bottom and left,right boundaries
                if i != 0:
                    if lights[i-1][j] == 1:
                        lights[i-1][j] = 0
                    else:
                        lights[i-1][j] = 1

                if i != 2:
                    if lights[i+1][j] == 1:
                        lights[i+1][j] = 0
                    else:
                        lights[i+1][j] = 1                
                    
                if j != 0:
                    if lights[i][j-1] == 1:
                        lights[i][j-1] = 0
                    else:
                        lights[i][j-1] = 1

                if j != 2:
                    if lights[i][j+1] == 1:
                        lights[i][j+1] = 0
                    else:
                        lights[i][j+1] = 1

        
    for i in range(3):
        for j in range(3):
            print(lights[i][j],end="")
        print()

if __name__ == '__main__':
    solve()