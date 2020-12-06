with open("./06/real.in") as f:
    assert 6521 == sum(
        map(lambda group: len(set(group.replace("\n", ""))), f.read().split("\n\n")),
    )
