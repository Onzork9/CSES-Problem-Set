def main():
    n = int(input())
    while n!=1:
        print(int(n), end=" ")
        if n%2==1:
            n=n*3+1
        else:
            n = n/2
    print(1)
if __name__ == "__main__":
    main()