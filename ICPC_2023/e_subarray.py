

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        a = list(map(int, input().split()))
        result = count_non_beautiful_subarrays(a)
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()