from pathlib import Path

f = Path("./input.txt")
lines = f.read_text().strip().splitlines()

# test = """
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# """.strip().splitlines()

# 2554


# part one

# def main(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     word = "XMAS"
#     word_len = len(word)
#     count = 0
#
#     # Directions: (dy, dx) -> (row change, col change)
#     directions = [
#         (-1, 0),
#         (1, 0),  # vertical (up, down)
#         (0, -1),
#         (0, 1),  # horizontal (left, right)
#         (-1, -1),
#         (1, 1),  # diagonal (\)
#         (-1, 1),
#         (1, -1),  # diagonal (/)
#     ]
#
#     def is_valid(r, c):
#         return 0 <= r < rows and 0 <= c < cols
#
#     def check_direction(r, c, dy, dx):
#         for i in range(word_len):
#             nr, nc = r + dy * i, c + dx * i
#             if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
#                 return False
#         return True
#
#     for r in range(rows):
#         for c in range(cols):
#             # Try to match the word starting at (r, c)
#             if grid[r][c] == word[0]:
#                 for dy, dx in directions:
#                     if check_direction(r, c, dy, dx):
#                         count += 1
#
#     return count
#


# part two

test = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip().splitlines()


def main(rows):
    ans = 0
    grid = [[char for char in row] for row in rows]

    for r in range(len(grid) - 2):
        for c in range(len(grid[r]) - 2):
            matrix = [[i for i in x[c : c + 3]] for x in grid[r : r + 3]]
            if (
                f"{matrix[0][0]}{matrix[1][1]}{matrix[2][2]}" == "MAS"
                or f"{matrix[0][0]}{matrix[1][1]}{matrix[2][2]}" == "SAM"
            ) and (
                f"{matrix[0][2]}{matrix[1][1]}{matrix[2][0]}" == "MAS"
                or f"{matrix[0][2]}{matrix[1][1]}{matrix[2][0]}" == "SAM"
            ):
                ans += 1

    return ans


result = main(test)

print(result)
