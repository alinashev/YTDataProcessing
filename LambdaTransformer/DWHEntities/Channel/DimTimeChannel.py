from datetime import datetime


class DimTimeChannel:
    def __init__(self) -> None:
        self.time_id: str = str(datetime.now().time())
        self.hour: int = datetime.now().hour
        self.minute: int = datetime.now().minute
        self.second: int = datetime.now().second

    def get_time_id(self) -> str:
        return self.time_id

    def get_hour(self) -> int:
        return self.hour

    def get_minute(self) -> int:
        return self.minute

    def get_second(self) -> int:
        return self.second

    def __str__(self) -> str:
        return 'time_id {time_id}' \
               '\nhour {hour}' \
               '\nminute {minute}' \
               '\nsecond {second}'.format(time_id=self.time_id,
                                          hour=self.hour,
                                          minute=self.minute,
                                          second=self.second)

    def to_dict(self) -> dict:
        return {
            'time_id': self.time_id,
            'hour': self.hour,
            'minute': self.minute,
            'second': self.second
        }
