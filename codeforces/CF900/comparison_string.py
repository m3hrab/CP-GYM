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
        s = input()

        if s[0]=='<':
            temp=[1,2]
            current = "<"
        else:
            temp = [2,1]
            current = ">"

        for i in range(1,n):
            if s[i] == '<':
                temp.append(temp[-1]+1)
            if s[i] == ">":
                temp.append(temp[-1]-1)


        print(len(set(temp)))


if __name__ == '__main__':
    solve()