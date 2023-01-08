for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr == arr.sort(reverse=True)
    old_arr = arr[:]

    flag = True
    not_reorder = True
    # Check the arr is ugly or not
    for j in range(1, len(arr)):
        if arr[j]==sum(arr[:j]):
            # try to make it beautiful
            for beauti in range(j+1,len(arr)):
                if arr[beauti] != sum(arr[:j]):
                    # swip the numbers 
                    temp = arr[j]
                    arr[j] = arr[beauti]
                    arr[beauti] = temp
                    flag = False 
                    break
            
            if flag:
                print("NO")
                not_reorder = False
                break 

    if flag != True or not_reorder==True:
        print("YES")
        for item in arr:
            print(item, end= ' ')
        print()
     
            