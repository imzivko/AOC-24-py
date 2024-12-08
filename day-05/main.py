import operator
from itertools import accumulate, count
from pathlib import Path

f = Path("./input.txt")

lines = f.read_text().split("\n\n")

# r = lines[0].split("\n")
# p = lines[1].split("\n")

r = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13""".split()

p = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split()


def part_two(ans, rules):
    out = []
    for page in ans:
        valid_page = []
        for page_num in page:
            valid_page_rules = list(
                filter(lambda rule: rule[0] == page_num and (rule[1] in page), rules)
            )

            if len(valid_page_rules):
                valid_page.append(list((map(lambda x: x[0], valid_page_rules))))

        sorted_lists = sorted(valid_page, key=len, reverse=True)

        res = [sublist[0] for sublist in sorted_lists]

        out.append(res)
    z = []
    for nums in out:
        mut = nums
        mut.append(0)
        z.append(mut)

    return z


def main(r, p):
    ans = []

    rules = [[int(rul) for rul in rule.split("|")] for rule in r]
    pages = [[int(page) for page in page.split(",")] for page in p]

    for page in pages:
        valid_page = False
        for page_num in page:
            page_rules = list(
                filter(lambda rule: rule[0] == page_num and (rule[1] in page), rules)
            )
            if len(page_rules) == len(page[page.index(page_num) + 1 : len(page)]):
                valid_page = True
            else:
                valid_page = False
                break
        # not - second part
        if not valid_page:
            ans.append(page)

    revalidated_lists = part_two(ans, rules)

    list_of_middle_page_numbers = list(
        map(lambda y: y[int(len(y) / 2)], revalidated_lists)
    )

    # expected to return sum of the middle page numbers from valid pages
    return list(accumulate(list_of_middle_page_numbers, operator.add))[-1]


result = main(r, p)
print(result)
