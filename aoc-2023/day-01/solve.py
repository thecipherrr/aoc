def parse():
    out = []
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("input.txt") as file:
        for line in file:
            parsed_line = []

            for i in range(len(line)):
                for idx, val in enumerate(numbers, 1):
                    if line[i:].startswith(val):
                        parsed_line.append(str(idx))
                if line[i].isnumeric():
                    parsed_line.append(line[i])

            out.append(parsed_line)

    return out


def solve(data):
    ans = 0
    for i in data:
        ans += int(i[0]) * 10 + int(i[-1])

    print(ans)


def main():
    data = parse()
    solve(data)


if __name__ == "__main__":
    main()

