from pathlib import Path

f = Path("./input.txt")
lines = f.read_text().strip().split()


def main(data):
    left = []
    right = []

    for idx, num in enumerate(data):
        if idx % 2 == 0:
            left.append(num)
        else:
            right.append(num)

    left.sort()
    right.sort()

    ans = 0

    for first, second in zip(left, right):
        # part one
        # ans += abs(int(first) - int(second))

        # part two
        ans += abs(int(first) * right.count(first))

    return ans


result = main(lines)

print(result)
