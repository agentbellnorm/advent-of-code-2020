import re


def direct_parents(tree, child):
    return [parent for parent in tree.keys() if child in tree[parent]]


def ancestors(tree, child):
    ancestors_list = []
    for parent in direct_parents(tree, child):
        ancestors_list.append(parent)
        ancestors_list += ancestors(tree, parent)

    return ancestors_list


bags = {}

with open("./07/real.in") as f:
    for rule in f.readlines():
        parent, *children = re.findall("(\w+ \w+) bag", rule)
        bags[parent] = children

    assert 300 == len(set(ancestors(bags, "shiny gold")))
