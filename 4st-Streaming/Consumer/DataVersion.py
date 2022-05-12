from datetime import datetime


class DataVersion:

    def get_date(self) -> str:
        return str(datetime.now().date())

    def get_hour(self) -> int:
        return datetime.now().hour

    def get_minute(self) -> int:
        return datetime.now().minute

    def get_month(self) -> int:
        return datetime.now().month
