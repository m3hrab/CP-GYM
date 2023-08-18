def main():
    # Input area
    for i in range(int(input())):
        grid = []
        temp = input()
        for _ in range(8):
            n = list(input())
            grid.append(n)

        
        for i in range(8):
            b = True
            r = True 
            for j in range(8):
                if grid[i][j] != 'R':
                    r = False 
                if grid[j][i] != 'B':
                    b = False

            if r:
                ans = "R"
            elif b:
                ans = "B"

        print(ans)



    # main codes

if __name__ == "__main__":
    main()
