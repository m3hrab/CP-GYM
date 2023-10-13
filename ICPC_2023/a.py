def count_non_beautiful_subarrays(arr):
    n = len(arr)
    result = n * (n + 1) // 2  # Total number of subarrays
    
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            continue
        result -= (i * (i + 1)) // 2  # Subtract the number of beautiful subarrays

    return result


