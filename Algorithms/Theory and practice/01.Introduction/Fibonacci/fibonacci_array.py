def fib(n):
    # put your code here
    if n < 3:
        return 1
    result_list = [None] * n
    result_list[0] = 1
    result_list[1] = 1
    for i in range(2, n):
        result_list[i] = result_list[i - 1] + result_list[i - 2]
    return result_list[n - 1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()