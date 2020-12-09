from itertools import combinations


def has_pair_that_sums(numbers, x):
    for a, b in combinations(numbers, 2):
        if a != b and a + b == x:
            return True
    return False


def find_encoding_error(numbers, preamble, idx):
    num = numbers[idx]
    nums = numbers[idx - preamble : idx]
    if not has_pair_that_sums(nums, num):
        return idx

    return find_encoding_error(numbers, preamble, idx + 1)


with open("./09/real.in") as f:
    numbers = list(map(int, f.read().splitlines()))
    invalid_number_index = find_encoding_error(numbers, 25, 25)

    invalid_number = numbers[invalid_number_index]
    interesting_numbers = numbers[: invalid_number_index + 1]

    encryption_weakness = None

    for idx, number in enumerate(interesting_numbers):
        current_range = interesting_numbers[idx:]
        for i, n in enumerate(current_range):
            possible_set = current_range[:i]
            if sum(possible_set) == invalid_number:
                encryption_weakness = min(possible_set) + max(possible_set)
                break

    assert encryption_weakness == 4389369