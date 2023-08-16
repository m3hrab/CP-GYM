n, k, l, c, d, p, nl, np = map(int, input().split())

drink = k*l 
toast_d = drink//nl
toast_c = c*d // 1
toast_s = p // np 

ans = min(toast_d, toast_c, toast_s)//n 
print(ans)