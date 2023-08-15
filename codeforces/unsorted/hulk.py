n = int(input())
n1 = "I hate "
n2 = "I love "
s = ""
for i in range(n):
    if i%2==0:
        s += n1 
    else:
        s += n2
    
    if n!=1 and i!=n-1:
        s += "that "
s += "it"
print(s)
