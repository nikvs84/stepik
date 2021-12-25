def gcd(a, b):
    while a != 0 or b != 0:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            if a > b:
                a = a % b
            elif b > a:
                b = b % a
            else:
                return a
    return 1


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()