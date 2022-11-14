import re
from functools import reduce


def valid(range_a, range_b, x):
    return (range_a[0] <= x <= range_a[1]) or (range_b[0] <= x <= range_b[1])


def get_totally_invalid(fields, ticket):
    totally_invalid = []
    for value in ticket:
        if not any(map(lambda rules: valid(rules[0], rules[1], value), fields)):
            totally_invalid.append(value)

    return totally_invalid


with open("./16/real.in") as f:
    fields, your_ticket, nearby_tickets = f.read().split("\n\n")

    fields = list(
        map(
            lambda field: list(
                map(
                    lambda rule: list(map(int, rule.split("-"))),
                    re.findall("\d*-\d*", field),
                )
            ),
            fields.splitlines(),
        )
    )
    your_ticket = your_ticket.splitlines()[1].split(",")
    nearby_tickets = list(
        map(lambda x: list(map(int, x.split(","))), nearby_tickets.splitlines()[1:])
    )

    v = 0
    for ticket in nearby_tickets:
        v += sum(get_totally_invalid(fields, ticket))

    assert 21956 == v
