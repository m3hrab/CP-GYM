import sys
import math

# Inputs
def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

# outputs
def print_int_list(arr):
    sys.stdout.write(' '.join(map(str, arr)) + '\n')
    sys.stdout.flush()


def is_sorted(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            return False

        if arr[mid] < arr[mid - 1]:
            return False

        left += 1
        right -= 1

    return True

def solve():
    for i in range(int(input())):
        n = read_int()
        arr = read_int_list()

        count = 0
        i = 0

        if is_sorted(arr):
            print("0")
            continue
        
        while True:
            arr[i] = max(0, arr[i]-1)
            if is_sorted(arr):
                print(count)
                break 
            count +=1
            if i == n-1:
                i = 0 
            else:
                i += 1


if __name__ == "__main__":
    solve()
