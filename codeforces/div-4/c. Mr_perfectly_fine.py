for i in range(int(input())):
    total_books = int(input())
    times = []
    skills = []
    for i in range(total_books):
        time, skill = input().split()
        times.append(int(time))    
        skills.append(skill)  

    skill_11 = []
    skill_10 = []
    skill_01 = []
    # save the indexes
    for i in range(total_books):
        if skills[i] == '11':
            skill_11.append(i)         
        elif skills[i] == '10':
            skill_10.append(i)         
        if skills[i] == '01':
            skill_01.append(i)

    flag1 = True
    flag2 = True
    flag3 = True

    if len(skill_11) == 0:
        flag1 = False
    if len(skill_10) == 0:
        flag2 = False
    if len(skill_01) == 0:
        flag3 = False
    # find the minimum time

    if flag1:
        min_ind = skill_11[0]
        for i in range(len(skill_11)):
            if times[skill_11[i]] < times[min_ind]:
                min_ind = skill_11[i]
        time_11 = times[min_ind]

    if flag2:
        min_ind = skill_10[0]
        for i in range(len(skill_10)):
            if times[skill_10[i]] < times[min_ind]:
                min_ind = skill_10[i]
        time_10 = times[min_ind]

    if flag3:
        min_ind = skill_01[0]
        for i in range(len(skill_01)):
            if times[skill_01[i]] < times[min_ind]:
                min_ind = skill_01[i]
        time_01 = times[min_ind]
    
    if flag1 == False and (flag2==False or flag3==False):
        print("-1")
    elif flag1 == True and (flag2==False and flag3==False):
        print(time_11)
    elif flag1 == True and flag2 == True and flag3 == True:
        if time_11 < (time_10+time_01):
            print(time_11)
        else:
            print(time_10+time_01)
    elif flag1 == False and flag2 == True and flag3 == True:
        print(time_01+time_10)
        