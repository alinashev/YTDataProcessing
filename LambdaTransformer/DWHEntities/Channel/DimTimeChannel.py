from datetime import datetime
from typing import Any


class DimTimeChannel:
    def __init__(self) -> None:
        self.time_id: str = str(datetime.now().date()) + "-" + str(datetime.now().hour)
        self.date: Any = datetime.now().date()
        self.year: int = datetime.now().year
        self.month: int = datetime.now().month
        self.day: int = datetime.now().day
        self.hour: int = datetime.now().hour
        self.week: int = datetime.now().date().isocalendar()[1]

    def get_time_id(self) -> str:
        return self.time_id

    def get_year(self) -> int:
        return self.year

    def get_month(self) -> int:
        return self.month

    def get_day(self) -> int:
        return self.day

    def get_hour(self) -> int:
        return self.hour

    def get_week(self) -> int:
        return self.week

    def __str__(self) -> str:
        return 'time_id {time_id}' \
               '\nyear {year}' \
               '\nmonth {month}' \
               '\nday {day}' \
               '\nhour {hour}' \
               '\nweek {week}'.format(time_id=self.time_id,
                                      date=self.date,
                                      year=self.year,
                                      month=self.month,
                                      day=self.day,
                                      hour=self.hour,
                                      week=self.week)

    def to_dict(self) -> dict:
        return {
            'time_id': self.time_id,
            'date': self.date,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'hour': self.hour,
            'week': self.week
        }
