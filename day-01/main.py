from pathlib import Path

p = Path('./input.txt')
f = p.read_text()

input_data = f.strip().split()

left = []
right = []

for idx, num in enumerate(input_data):
    if idx % 2 == 0:
        left.append(num)
    else:
        right.append(num)

left.sort()
right.sort()

out = 0

for first, second in zip(left, right):
    # part one
    # out += abs(int(first) - int(second))

    # part two
    out += abs(int(first) * right.count(first))


print(out)

