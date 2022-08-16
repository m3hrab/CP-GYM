def into_min(h, m):
    return h*60 + m

for i in range(int(input())):
    n, h, m = map(int, input().split())

    bed_time = into_min(h, m) 
    alarm = []
    for i in range(n):
        alarm.append(list(map(int, input().split())))


    temp = []
    for time in alarm:
        new = into_min(time[0], time[1])
        if new<bed_time:
            new += 24*60
        temp.append(new)
        

    time = min(temp)
    r = time - bed_time
    h = r//60
    m = r%60

    print("%d %d"%(h, m))
    