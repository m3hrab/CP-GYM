n = int(input())
cards = list(map(int, input().split()))
indexes = [i for i in range(1,n+1)]

# Sorting the cards array
for i in range(n):
    for j in range(i, n):
        if cards[i] > cards[j]:
            temp = cards[i] 
            cards[i] = cards[j]
            cards[j] = temp 

            temp2 = indexes[i]
            indexes[i] = indexes[j]
            indexes[j] = temp2

for i in range(n//2):
    print("%d %d"%(indexes[i], indexes[-(i+1)]))
