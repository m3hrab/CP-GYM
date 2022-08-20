n = int(input())
t = 0
flag = 1
for i in range(1,n+1):
    # if flag==1:
    #     t -= i
    #     flag = 0
    # else:
    #     t += i
    #     flag = 1
    t += i*(-1)**i
print(t)

