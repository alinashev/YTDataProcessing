from datetime import datetime


class DimDateChannel:
    def __init__(self) -> None:
        self.date_id: str = str(datetime.now().date())
        self.year: int = datetime.now().year
        self.month: int = datetime.now().month
        self.day: int = datetime.now().day
        self.week: int = datetime.now().date().isocalendar()[1]

    def get_date_id(self) -> str:
        return self.date_id

    def get_year(self) -> int:
        return self.year

    def get_month(self) -> int:
        return self.month

    def get_day(self) -> int:
        return self.day

    def get_week(self) -> int:
        return self.week

    def __str__(self) -> str:
        return 'date_id {date_id}' \
               '\nyear {year}' \
               '\nmonth {month}' \
               '\nday {day}' \
               '\nweek {week}'.format(date_id=self.date_id,
                                      year=self.year,
                                      month=self.month,
                                      day=self.day,
                                      week=self.week)

    def to_dict(self) -> dict:
        return {
            'date_id': self.date_id,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'week': self.week
        }
