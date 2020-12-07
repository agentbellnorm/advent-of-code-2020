import re


def bags_in_bag(tree, bag):
    children = tree[bag]

    if not children:
        return 1

    branches = 0
    for child in children:
        branches += child["n"] * bags_in_bag(tree, child["color"])

    return branches + 1


bags = {}

with open("./07/real.in") as f:
    for rule in f.readlines():
        parent, *children = re.findall("((\d+ )?\w+ \w+) bag", rule)
        children = [match[0] for match in children if "no other" not in match[0]]
        parent = parent[0]
        fixed = []
        for child in children:
            n, color = child.split(" ", 1)
            fixed.append({"n": int(n), "color": color})
        bags[parent] = fixed

    assert 8030 == bags_in_bag(bags, "shiny gold") - 1
