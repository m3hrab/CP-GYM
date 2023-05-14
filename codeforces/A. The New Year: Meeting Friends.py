point = list(map(int, input().split()))
mid = sorted(point)[1]
total = abs(mid-point[0])+abs(mid-point[1])+abs(mid-point[2])
print(total)