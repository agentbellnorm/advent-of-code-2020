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
    invalid_number = numbers[find_encoding_error(numbers, 25, 25)]
    assert invalid_number == 29221323
