for i in range(int(input())):
    s = input()
    if len(s)%6 != 0:
        over = len(s)//6 
        ball_left = (len(s) - (6*over)) / 10
        over += ball_left
    else:
        over = len(s)//6

    wicket = 0
    run = 0 

    for i in s:
        if i == 'W':
            wicket += 1
        else:
            run += int(i)
        
    
    if over > 1:
        a1 = "Overs"
    else:
        a1 = "Over"

    if run > 1:
        a2 = "Runs"
    else:
        a2 = "Run"
    
    if wicket > 1:
        a3 = "Wickets."
    else:
        a3 = "Wicket."

    print("%.1f %s %d %s %d %s"%(over, a1, run, a2, wicket, a3))
