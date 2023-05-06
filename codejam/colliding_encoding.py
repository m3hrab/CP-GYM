def bisect_left(list, item):
    left, right = 0, len(list)
    while left < right:
        mid = (left + right) // 2
        if list[mid] < item:
            left = mid + 1
        else:
            right = mid
    return left

def bisect_right(list, item):
    left, right = 0, len(list)
    while left < right:
        mid = (left + right) // 2
        if list[mid] <= item:
            left = mid + 1
        else:
            right = mid
    return left

def is_unique(list, item):
    list.sort()
    index = bisect_left(list, item)
    if index == len(list) or list[index] != item:
        return False
    return index == bisect_right(list, item) - 1


letters = [chr(letter) for letter in range(65,91)]
for i in range(int(input())):
    digits = list(map(int, input().split()))
    words = []
    colid = []
    for j in range(int(input())):
        words.append(input())

    flag = False 
    for word in words:
        digit = ''
        for letter in word:
            digit += str(digits[letters.index(letter)])

        if is_unique(colid, digit):
            colid.append(digit)
        else:
            flag = True
            break

    # # check repeated word 
    # flag = False 
    # for d in colid:
    #     if is_unique(colid,d) == False:
    #         flag = True 
    #         break 

    if flag:
        print("Case #%d: YES"%(i+1))
    else:
        print("Case #%d: NO"%(i+1))