for i in range(int(input())):
    arr_length = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    for i in range(10):
        if i not in arr:
            new_arr.append(i)
    count = 0
    for i in range(len(new_arr)):
        for j in range(i+1,len(new_arr)):
            count += 1

    print(count*6)