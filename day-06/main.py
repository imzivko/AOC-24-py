from pathlib import Path

f = Path("./input.txt")

test = f.read_text().splitlines()

print(test[52][48])


# test = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.strip().splitlines()

# 41


def visualize(coords):
    test_copy = [[x for x in k] for k in test]

    for x, y in coords:
        if x and y:
            test_copy[y][x] = test_copy[y][x].replace(".", "x")

    for ds in test_copy:
        print("".join(ds))


def find_initial_cords(rows):
    for idx, r in enumerate(rows):
        if "^" in r:
            return r.index("^"), idx


def main(grid):
    pos = []
    rows = len(grid)
    cols = len(grid[0])

    init_x, init_y = find_initial_cords(grid)

    def is_out(c, r):
        print(c, r)
        # here
        return r < 0 or r >= rows - 1 or c < 0 or c >= cols - 1

    directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]

    # first is always up
    current_direction = 0

    def rotate_direction():
        nonlocal current_direction
        current_direction = (current_direction + 1) % 4

    def move(x, y):
        nonlocal current_direction

        if is_out(x, y):
            print("out")
            return False

        pos.append((x, y))

        if (
            grid[y + directions[current_direction][1]][
                x + directions[current_direction][0]
            ]
            == "#"
        ):
            rotate_direction()

        dx, dy = directions[current_direction]
        return move(x + dx, y + dy)

    move(init_x, init_y)

    print(pos)
    visualize(pos)

    with f.open("w") as file:
        for line in grid:
            file.write(line + "\n")

    return len(set(pos)) + 1


result = main(test)
print(result)
