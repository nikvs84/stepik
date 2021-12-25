import math

def fib_mod(n, m):
    return fib_mod_simple(n, m)

def fib_mod_simple(n, m):
    """Выяснилось, что функция остатков по подулю от последовательности Фибоначчи имеет период :-)"""
    if n < 3:
        return 1
    prev_remainder = 1
    prev_prev_remainder = 1
    current = 0
    counter = 0
    period = 2
    is_period_founded = False
    periodic_reminders = [1, 1]
    for i in range(3, n + 1):
        counter += 1
        current = (prev_remainder + prev_prev_remainder)
        if current >= m:
            current = current % m
        if not is_period_founded:
            period += 1
            periodic_reminders.append(current)
        prev_prev_remainder = prev_remainder
        prev_remainder = current
        # print(right_justify(i, 3) + ': ' + right_justify(current))
        if current == 0:
            # print('-------------------- ' + str(counter))
            counter = 0
            if prev_prev_remainder == 1:
                is_period_founded = True
                # print('========================================' + str(period))
                return get_reminder_from_periodic_values(periodic_reminders, n)

    return current


def get_reminder_from_periodic_values(periodic_values, original_number_of_fibonacci_items):
    period = len(periodic_values)
    index = (original_number_of_fibonacci_items % period) - 1
    return periodic_values[index]


def right_justify(d, count = 7):
    """Изначально использовалась для вывода значений остатков по модулю, чтобы найти какую-то закономерность. Используется для отладки."""
    return ('%(number)' + str(count) + 'd') % {'number': d}


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()