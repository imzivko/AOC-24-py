from pathlib import Path

p = Path('./input.txt')
f = p.read_text()

input_data = f.strip().splitlines()

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
def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def main(data):
    levels = [list(map(int, row.split())) for row in data]

    safe_count = 0
    for level in levels:
        if is_safe(level) or is_safe_with_dampener(level):
            safe_count += 1

    return safe_count


result = main(input_data)
print(result)