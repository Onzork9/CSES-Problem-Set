def main(): 
    total_elements = int(input())
    n = list(map(int, input().split()))[:total_elements]

    prev_ele = n[0]
    output = 0

    for i in n[1:]:
        if i < prev_ele:
            output += prev_ele - i
        else:
            prev_ele = i

    print(output)

if __name__ == "__main__":
    main()