def solve():
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    arr = []
    ans = 0
    with open("input.txt") as file:
        for i in file:
            arr = []
            for j in i:
                if j.isnumeric():
                    arr.append(int(j))
                if j == "\n":
                    ans += arr[0] * 10 + arr[-1]
    print(ans)


def main():
    solve()


if __name__ == "__main__":
    main()

