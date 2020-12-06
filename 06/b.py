from functools import reduce

with open("./06/real.in") as f:
    assert 3305 == sum(
        map(
            lambda group: len(
                reduce(
                    set.intersection,
                    [set(item) for item in set(group.splitlines())],
                )
            ),
            f.read().split("\n\n"),
        ),
    )