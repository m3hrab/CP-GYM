n = int(input())
for i in range(n):
    s = input()
    overs = len(s) // 6
    extra_balls = len(s) % 6
    if extra_balls > 0:
        overs += extra_balls / 10

    runs = 0
    wickets = 0
    for c in s:
        if c == 'W':
            wickets += 1
        else:
            runs += int(c)

    print(f"{overs:.1f} {'Overs' if overs > 1 else 'Over'} {runs} {'Runs' if runs > 1 else 'Run'} {wickets} {'Wickets' if wickets > 1 else 'Wicket'}.")

