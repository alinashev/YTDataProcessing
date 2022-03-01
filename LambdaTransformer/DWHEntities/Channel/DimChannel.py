class DimChannel:
    def __init__(self, channel_id: str, channel_name: str) -> None:
        self.channel_id: str = channel_id
        self.channel_name: str = channel_name

    def __str__(self) -> str:
        return 'channel_id {channel_id}' \
               '\nchannel_name {channel_name}'.format(channel_id=self.channel_id,
                                                      channel_name=self.channel_name)

    def to_dict(self) -> dict:
        return {
            'channel_id': self.channel_id,
            'channel_name': self.channel_name
        }
