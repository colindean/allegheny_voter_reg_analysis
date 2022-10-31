import datetime
from datetime import timedelta

ONE_DAY = 1
ONE_YEAR = 365 * ONE_DAY
EIGHT_YEARS = 8 * ONE_YEAR

JANUARY = 1


def beginning_of_year(dt: datetime.datetime):
    return dt.replace(month=JANUARY, day=1, hour=0, minute=0, second=0, microsecond=0)


def beginning_of_eight_years_ago():
    return beginning_of_year(datetime.datetime.now() - timedelta(days=EIGHT_YEARS))
