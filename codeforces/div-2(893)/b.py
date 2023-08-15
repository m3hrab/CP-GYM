# Main function
def main():
    # Input reading
    n = int(input())
    for i in range(n):
        a,b,c = map(int, input().split())
        if a>b:
            print("First")
        elif a<b:
            print("Second")
        else:
            t = c%2
            if t:
                print("First")
            else:
                print("Second")
            

if __name__ == "__main__":
    main()
