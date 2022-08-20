count = 0
temp = 0
for i in range(int(input())):
    magnet = int(input())
    # initialization 
    # if len(magnets) == 0:
    #     magnets.append(magnet)
    #     continue
    # if magnets[-1][-1] != magnet[0]:
    #     magnets[-1] = magnets[-1] + magnet
    # else:
    #     magnets.append(magnet)
    if temp == 0:
        temp = magnet
        count += 1
    if magnet != temp:
        count += 1
        temp = magnet
    
        
# print(len(magnets))
print(count)