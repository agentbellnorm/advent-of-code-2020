import re
from functools import reduce


def valid(rule, value):
    return (rule[0][0] <= value <= rule[0][1]) or (rule[1][0] <= value <= rule[1][1])


def invalid(fields, ticket):
    for value in ticket:
        if not any(map(lambda rules: valid(rules, value), fields)):
            return True

    return False


""" def valid(rule, values):
    for value in values:
        if not valid(rule, value):
            return False
    return True """


def parse_rules(lines):
    rules = {}
    for line in lines:
        attribute = re.search("^(.*):", line).group(1)
        rule = list(
            map(
                lambda rule: list(map(int, rule.split("-"))),
                re.findall("\d*-\d*", line),
            )
        )
        rules[attribute] = rule
    return rules



with open("./16/real.in") as f:
    fields, your_ticket, nearby_tickets = f.read().split("\n\n")

    rules = parse_rules(fields.splitlines())
    your_ticket = list(map(int, your_ticket.splitlines()[1].split(",")))
    nearby_tickets = list(
        map(lambda x: list(map(int, x.split(","))), nearby_tickets.splitlines()[1:])
    )

    tickets_to_check = list(
        filter(lambda ticket: not invalid(rules.values(), ticket), nearby_tickets)
    )
    tickets_to_check.insert(0, your_ticket)
    # print(tickets_to_check)

    field_order = {}

    for col_index, my_ticket_value in enumerate(your_ticket):
        found_rule = ""
        for ticket in tickets_to_check:
            check = ticket[col_index]
            for rule_name in rules.keys():
                
            if all_colums_valid:
                print("seems like position {} is {}".format(col_index, rule_name))
                field_order[rule_name] = my_ticket_value
                break

    print(len(field_order.keys()))

    print(
        reduce(
            lambda acc, rule: acc * field_order[rule] if "departure" in rule else acc,
            field_order.keys(),
            1,
        )
    )
