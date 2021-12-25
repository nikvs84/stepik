import math


def primes():
    current = 2
    yield current

    def is_prime(num):
        if num % 2 == 0:
            return False
        for i in range(3, round(math.sqrt(num) + 1), 2):
            if num % i == 0:
                return False
        return True

    while True:
        current += 1
        if is_prime(current):
            yield current
