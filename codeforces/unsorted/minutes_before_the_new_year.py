for i in range(int(input())):
    a,b = map(int, input().split())
    time = 1440-((a*60)+b)
    print(time)