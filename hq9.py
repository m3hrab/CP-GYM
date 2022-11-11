p = input()
hq = ['H','Q','9', '+']
signal = True

for letter in p:
    if letter in hq:
        print('YES')
        signal = False 
        break 
if signal:
    print("NO")     