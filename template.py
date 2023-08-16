import sys

# Inputs
def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

# outputs
def print_int_list(arr):
    sys.stdout.write(' '.join(map(str, arr)) + '\n')
    sys.stdout.flush()

# Main function
def main():
    # Input area
    n = read_int()
    arr = read_int_list()

    # main codes

if __name__ == "__main__":
    main()
