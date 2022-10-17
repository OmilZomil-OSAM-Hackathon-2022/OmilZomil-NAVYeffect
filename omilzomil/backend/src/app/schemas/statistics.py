from datetime import datetime


class Date(datetime):
    def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        cls.day = day
        return super().__new__(cls, year, month, day and day or 1)

    def __repr__(self):
        L = [self.year, self.month, self.day]
        return "%s(%s)" % (self.__class__.__qualname__, ", ".join(map(str, L)))

    def __str__(self):
        return self.strftime(self.day and "%Y-%m-%d" or "%Y-%m")

    @classmethod
    def now(cls, tz=None, day=True):
        cls = super().now(tz)
        if not day:
            cls.day = None
        return cls
