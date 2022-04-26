class FactChannel:
    def __init__(self, channel_id: str,  time_id: str, view_count: int,
                 subscriber_count: int, video_count: int) -> None:
        self.channel_id: str = channel_id
        self.time_id: str = time_id

        self.view_count: int = view_count
        self.subscriber_count: int = subscriber_count
        self.video_count: int = video_count

    def __str__(self) -> str:
        return 'channel_id {channel_id}' \
               '\ntime_id {time_id}' \
               '\nview_count {view_count}' \
               '\nsubscriber_count {subscriber_count}' \
               '\nvideo_count {video_count}'.format(channel_id=self.channel_id,
                                                    time_id=self.time_id,
                                                    view_count=self.view_count,
                                                    subscriber_count=self.subscriber_count,
                                                    video_count=self.video_count)

    def to_dict(self) -> dict:
        return {
            'channel_id': self.channel_id,
            'time_id': self.time_id,
            'view_count': self.view_count,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count
        }
