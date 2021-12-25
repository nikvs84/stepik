class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, n) -> None:
        if n <= 0:
            raise NonPositiveError
        else:
            super(PositiveList, self).append(n)
