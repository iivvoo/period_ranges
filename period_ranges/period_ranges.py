from dateutil.relativedelta import relativedelta, SU
from datetime import datetime


class Period:
    DAY = 1
    WEEK = 2
    MONTH = 3
    QUARTER = 4
    YEAR = 5

    def __init__(self, start, end, type=MONTH):
        self.start = start
        self.end = end
        self.type = type

    @property
    def week(self):
        return self.start.isocalendar()[1]

    @property
    def month(self):
        return self.start.month

    @property
    def year(self):
        return self.start.year

    @property
    def quarter(self):
        if self.month < 4:
            return 1
        if self.month < 7:
            return 2
        if self.month < 10:
            return 3
        return 4

    def __contains__(self, dt):
        return self.start <= dt <= self.end

    def __str__(self):
        if self.type == self.DAY:
            return "Day {0}".format(self.start)
        if self.type == self.WEEK:
            return "Week {0} of year {1}".format(self.week, self.year)
        if self.type == self.MONTH:
            return "Month {0} of year {1}".format(self.month, self.year)
        if self.type == self.QUARTER:
            return "Quarter {0} of year {1}".format(self.quarter, self.year)
        if self.type == self.YEAR:
            return "Year {0}".format(self.year)

        return 'Unknown period ${0}-${1}'.format(self.start, self.end)

    __repr__ = __str__


def generate_range(start, end=None, type=Period.MONTH, FIRST_DAY_OF_WEEK=SU):
    end = end or start

    if type == Period.DAY:
        inv_start = start
        interval = relativedelta(days=1)

    if type == Period.WEEK:
        inv_start = start + relativedelta(weekday=FIRST_DAY_OF_WEEK(-1))
        interval = relativedelta(weeks=1)

    elif type == Period.MONTH:
        inv_start = datetime(start.year, start.month, 1)
        interval = relativedelta(months=1)

    elif type == Period.QUARTER:
        first_month_of_quarter = ((start.month - 1) // 3) * 3 + 1
        inv_start = datetime(start.year, first_month_of_quarter, 1)
        interval = relativedelta(months=3)

    elif type == Period.YEAR:
        inv_start = datetime(start.year, 1, 1)
        interval = relativedelta(years=1)

    while end >= inv_start:
        inv_end = inv_start + interval - \
            relativedelta(seconds=1)
        yield Period(inv_start, inv_end, type)
        inv_start += interval


if __name__ == '__main__':
    import pprint

    start = datetime(2015, 11, 23, 0, 0, 0)
    end = datetime(2016, 4, 1, 0, 0, 0)

    print("Weeks")
    week = generate_range(start, end, Period.WEEK)

    pprint.pprint(list(week))

    print("Months")
    months = generate_range(start, end, Period.MONTH)

    pprint.pprint(list(months))

    print("Quarters")
    quarter = generate_range(start, end, Period.QUARTER)

    pprint.pprint(list(quarter))

    print("Years")
    years = list(generate_range(start, end, Period.YEAR))

    pprint.pprint(years)

    print(datetime(2014, 1, 1) in years[0])
    print(datetime(2015, 1, 1) in years[0])
    print(datetime(2016, 1, 1) in years[0])
    print(datetime(2017, 1, 1) in years[0])
