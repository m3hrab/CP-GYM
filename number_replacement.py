def make_uniqe(n):
    m = []
    for i in range(len(n)):
        if n[i] not in m:
            m.append(n[i])
            
    return m

for i in range(int(input())):
    temp = int(input())
    numbers = list(map(int, input().split()))
    string = list(input())
    new = {}
    if len(numbers) == len(string):
        for j in range(len(numbers)):
            if numbers[j] in new.keys():
                if new[numbers[j]] != string[j]:
                    print("NO")
                    break
            else:
                new[numbers[j]] = string[j]
        else:
            print("YES")
    else:
        print("NO")