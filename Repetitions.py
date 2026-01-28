def main():
    n = input()

    temp = None
    count = 0
    max_count = 0

    for ch in n:
        if ch == temp:
            count += 1
        else:
            count = 1  # reset to 1 because this char starts a new streak

        max_count = max(max_count, count)
        temp = ch

    print(max_count)
    
if __name__ == "__main__":
    main()
