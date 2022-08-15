username = list(input().lower())

new = []
for char in username:
    if char not in new:
        new.append(char)

if len(new)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")