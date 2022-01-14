class ChannelsID:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_channels_id(self) -> list:
        return [x.strip() for x in open("channels.txt", encoding='utf-8')]
