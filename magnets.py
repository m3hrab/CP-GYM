magnets = []
for i in range(int(input())):
    magnet = input()
    # initialization 
    if len(magnets) == 0:
        magnets.append(magnet)
        continue
    if magnets[-1][-1] != magnet[0]:
        magnets[-1] = magnets[-1] + magnet
    else:
        magnets.append(magnet)

print(len(magnets))