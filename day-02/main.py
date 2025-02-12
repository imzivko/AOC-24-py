from pathlib import Path

f = Path("./input.txt")
lines = f.read_text().strip().splitlines()


def is_safe(levels):
    increasing = True
    decreasing = True

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
        if levels[i] >= levels[i + 1]:
            increasing = False
        if levels[i] <= levels[i + 1]:
            decreasing = False

    return increasing or decreasing


# part two
def is_safe_with_dampener(level):
    for i in range(len(level)):
        modified_level = level[:i] + level[i + 1 :]
        if is_safe(modified_level):
            return True
    return False


def main(data):
    levels = [list(map(int, row.split())) for row in data]

    safe_count = 0
    for level in levels:
        if is_safe(level) or is_safe_with_dampener(level):
            safe_count += 1

    return safe_count


result = main(lines)

print(result)
