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
    n = read_int()
    goals = []
    teams = []
    for i in range(n):
        team = read_str()
        if team not in teams:
            teams.append(team)

        goals.append(team)

    if len(teams) > 1:
        if goals.count(teams[0]) > goals.count(teams[1]):
            print(teams[0])
        else:
            print(teams[1])
    else:
        print(teams[0])

if __name__ == '__main__':
    solve()