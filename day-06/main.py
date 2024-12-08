from pathlib import Path

f = Path("./input.txt")

test = f.read_text().splitlines()


def visualize(coords):
    test_copy = [[x for x in row] for row in test]

    for x, y in coords:
        if 0 <= x < len(test_copy[0]) and 0 <= y < len(test_copy):
            test_copy[y][x] = test_copy[y][x].replace(".", "X")

    for row in test_copy:
        print("".join(row))


def find_initial_cords(rows):
    for idx, row in enumerate(rows):
        if "^" in row:
            return row.index("^"), idx
    return None, None


def main(grid):
    pos = []
    rows = len(grid)
    cols = len(grid[0])

    init_x, init_y = find_initial_cords(grid)

    def is_out(c, r):
        return r < 0 or r >= rows or c < 0 or c >= cols

    directions = [
        (0, -1),  # Up
        (1, 0),  # Right
        (0, 1),  # Down
        (-1, 0),  # Left
    ]

    current_direction = 0

    def rotate_direction():
        nonlocal current_direction
        current_direction = (current_direction + 1) % 4

    def move(x, y):
        nonlocal current_direction

        dx, dy = directions[current_direction]
        next_x, next_y = x + dx, y + dy

        if is_out(next_x, next_y):
            return False

        if grid[next_y][next_x] == "#":
            rotate_direction()
            return move(x, y)

        pos.append((next_x, next_y))

        return True

    x, y = init_x, init_y
    pos.append((x, y))

    while move(x, y):
        dx, dy = directions[current_direction]
        x, y = x + dx, y + dy

    visualize(pos)

    return len(set(pos))


result = main(test)
print(result)
