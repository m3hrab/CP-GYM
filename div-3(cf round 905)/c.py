import bisect

def min_operations_to_non_decreasing(n, arr):
    operations = 0

    for i in range(1, n):
        target = arr[i - 1]
        while arr[i] < target:
            power = bisect.bisect_left(range(1, 31), max(target // arr[i], 1)) - 1
            operations += 1 << max(power, 0)
            target = arr[i] << max(power, 0)

    return operations

# Example usage:
t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Elements of the array

    result = min_operations_to_non_decreasing(n, arr)
    print(result)
