def main():
    n = int(input())
    if n == 2 or n == 3:
        print("NO SOLUTION")
        return
    list_of_numbers = [[], []]
    for i in range(1,n+1):
        if i % 2 == 0:
            list_of_numbers[0].append(i)
        else:
            list_of_numbers[1].append(i)

    print(*list_of_numbers[0], *list_of_numbers[1])


if __name__ == "__main__":
    main()