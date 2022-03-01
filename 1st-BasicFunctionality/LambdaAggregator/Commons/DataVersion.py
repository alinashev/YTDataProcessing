from datetime import datetime


class DataVersion:
    def __init__(self) -> None:
        self.date = None
        self.day = None
        self.hour = None

    def get_date(self) -> str:
        if not self.date:
            self.date = str(datetime.now().date())
        return self.date

    def get_day(self) -> str:
        if not self.day:
            self.day = str(datetime.now().day)
        return self.day

    def get_hour(self) -> str:
        if not self.hour:
            self.hour = str(datetime.now().hour)
        return self.hour
