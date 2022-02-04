class ChannelsID:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def get_channels_id(self) -> dict:
        return {line.split()[0]: line.split()[1] for line in open(self.file_name)}
