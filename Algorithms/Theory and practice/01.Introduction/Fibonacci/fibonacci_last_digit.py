def fib_digit(n):
    if n < 3:
        return 1
    prev_digit = 1
    prev_prev_digit = 1
    current = 0
    for i in range(3, n + 1):
        current = (prev_digit + prev_prev_digit) % (10)
        prev_prev_digit = prev_digit
        prev_digit = current
    return current


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()