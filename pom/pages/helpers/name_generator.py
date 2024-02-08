from random import choice, randrange
from string import ascii_letters


def get_random_name() -> str:
    # - Generate and return and random name
    return ''.join([choice(ascii_letters) for _ in range(randrange(5, 12))])


def get_random_path() -> str:
    # - Generate a random path using random names
    return '/'.join(
        [get_random_name() for _ in range(randrange(2, 5))]
    )