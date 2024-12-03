import re
from pathlib import Path
from itertools import accumulate

f = Path('./input.txt')
lines = f.read_text()

def filter_list(data):
    filtered_list = []
    is_inside_dont = False

    for line in data:
        if line == "don't()":
            is_inside_dont = True
        elif line == "do()":
            is_inside_dont  = False
            continue
        if not is_inside_dont:
            filtered_list.append(line)

    return filtered_list


def main(data):
    pairs = re.findall(r"\d+,\d+|do\(\)|don't\(\)", "".join(re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)))

    # part two pairs
    filtered_pairs = filter_list(pairs)

    pair_factors = []
    for i in range(len(filtered_pairs)):
        pair = filtered_pairs[i].split(",")
        pair_factors.append(int(pair[0]) * int(pair[1]))

    ans = list(accumulate(pair_factors))[-1]

    return ans

result = main(lines)

print(result)