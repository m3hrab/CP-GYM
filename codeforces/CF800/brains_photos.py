n, m = map(int, input().split())

colors = 'CMY'
colored_photo = False
not_tested = True 
for i in range(n):
    n = input()
    if not_tested:
        for i in n: 
            if i in colors:
                colored_photo = True 
                not_tested = False 
                break 


if colored_photo:
    print("#Color")
else:
    print("#Black&White")