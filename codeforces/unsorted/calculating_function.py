n = int(input())
if n%2==0:
    x = n//2 
    temp = x*(x+1) 
    temp2 = (n-x)**2
    print(temp-temp2)
else:
    x = n//2 + 1
    temp = x*(x+1) 
    temp2 = x**2
    print(temp2-temp)


 