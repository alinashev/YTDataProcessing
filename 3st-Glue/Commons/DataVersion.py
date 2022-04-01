from datetime import datetime


class DataVersion:
    def __init__(self) -> None:
        self.date = None
        self.hour = None
        self.year = None
        self.month = None

    def get_date(self) -> str:
        if not self.date:
            self.date = str(datetime.now().date())
        return self.date

    def get_hour(self) -> str:
        if not self.hour:
            self.hour = str(datetime.now().hour) + "h"
        return self.hour

    def get_year(self) -> int:
        if not self.year:
            self.year = datetime.now().year
        return self.year

    def get_month(self) -> int:
        if not self.month:
            self.month = datetime.now().month
        return self.month
