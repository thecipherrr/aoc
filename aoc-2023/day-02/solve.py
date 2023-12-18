import math


def part1():
    threshold = {"red": 12, "green": 13, "blue": 14}
    poss = 0

    with open("input.txt") as data:
        for line in data:
            game_idx, sets = line.split(": ")

            groups = map(str.split, sets.replace(";", ",").split(", "))
            if all(int(num) <= threshold[colors] for num, colors in groups):
                poss += int(game_idx.split(" ")[1])

    print(poss)


def part2():
    ans = 0

    with open("input.txt") as data:
        for line in data:
            cube_count = {"red": 0, "green": 0, "blue": 0}
            _, sets = line.split(": ")
            sets = sets.split("; ")

            for i in sets:
                i = {color: int(num) for num, color in map(str.split, i.split(", "))}
                cube_count = {
                    color: max(num, i.get(color, 0))
                    for color, num in cube_count.items()
                }
            ans += math.prod(cube_count.values())
        print(ans)


def main():
    part2()


if __name__ == "__main__":
    main()

