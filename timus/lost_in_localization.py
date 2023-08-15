def localize_monsters(number):
    if number >= 1 and number <= 4:
        return "few"
    elif number >= 5 and number <= 9:
        return "several"
    elif number >= 10 and number <= 19:
        return "pack"
    elif number >= 20 and number <= 49:
        return "lots"
    elif number >= 50 and number <= 99:
        return "horde"
    elif number >= 100 and number <= 249:
        return "throng"
    elif number >= 250 and number <= 499:
        return "swarm"
    elif number >= 500 and number <= 999:
        return "zounds"
    elif number >= 1000:
        return "legion"

number = int(input())

result = localize_monsters(number)

print(result)
