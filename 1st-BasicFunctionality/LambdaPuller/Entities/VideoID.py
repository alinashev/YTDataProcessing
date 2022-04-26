class VideoID:

    def __init__(self, channel_name: str, channel_id: str, video_id: str) -> None:
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.video_id = video_id

    def __str__(self) -> str:
        return 'channel_name {channel_name}' \
               '\nchannel_id {channel_id}' \
               '\nvideo_id {video_id}'.format(channel_name=self.channel_name,
                                              channel_id=self.channel_id,
                                              video_id=self.video_id)

    def to_dict(self):
        return {
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'video_id': self.video_id
        }

    def get_channel_name(self) -> str:
        return self.channel_name

    def get_channel_id(self) -> str:
        return self.channel_id

    def get_video_id(self) -> str:
        return self.video_id
