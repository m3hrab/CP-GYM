def bisect_left(lst, item):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < item:
            left = mid + 1
        else:
            right = mid
    return left

def bisect_right(lst, item):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= item:
            left = mid + 1
        else:
            right = mid
    return left

def is_unique(lst, item):
    lst.sort()
    index = bisect_left(lst, item)
    if index == len(lst) or lst[index] != item:
        return False
    return index == bisect_right(lst, item) - 1

a = [12,3,12]
print(is_unique([],3))