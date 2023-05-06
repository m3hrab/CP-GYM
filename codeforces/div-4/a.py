for i in range(int(input())):
    s1 = input()
    s2 = "codeforces"
    diff = 0
    for i in range(10):
        if s1[i] != s2[i]:
            diff += 1
    print(diff)