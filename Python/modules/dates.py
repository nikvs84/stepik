import datetime


def calculate(dt_original_str, delta_days_str):
    return format_date(calculate_dt(dt_original_str, delta_days_str))


def format_date(dt_source):
    return dt_source.strftime("%Y %-m %-d")


def calculate_dt(dt_original_str, delta_days_str):
    dt_start = datetime.datetime.strptime(dt_original_str, "%Y %m %d")
    delta_days = datetime.timedelta(int(delta_days_str))
    return dt_start.date() + delta_days


if __name__ == '__main__':
    date_str = input()
    delta_str = input()

    print(calculate(date_str, delta_str))
