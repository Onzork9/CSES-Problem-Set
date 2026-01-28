def main():
    list_len_input = int(input())
    list_input = list(map(int, input().split()))
    n = sum(list(range(0, list_len_input+1))) - sum(list_input)
    print(n)

if __name__ == "__main__":
    main()