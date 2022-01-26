class FactVideo:
    def __init__(self, video_id: str, date_id: str, time_id: str,
                 view_count: int, like_count: int, comment_count: int) -> None:
        self.video_id: str = video_id
        self.date_id: str = date_id
        self.time_id: str = time_id
        self.view_count: int = view_count
        self.like_count: int = like_count
        self.comment_count: int = comment_count

    def __str__(self) -> str:
        return 'video_id {video_id}' \
               '\ndate_id {date_id}' \
               '\ntime_id {time_id}' \
               '\nview_count {view_count}' \
               '\nlike_count {like_count}' \
               '\ncomment_count {comment_count}'.format(video_id=self.video_id,
                                                        date_id=self.date_id,
                                                        time_id=self.time_id,
                                                        view_count=self.view_count,
                                                        like_count=self.like_count,
                                                        comment_count=self.comment_count)

    def to_dict(self) -> dict:
        return {
            'video_id': self.video_id,
            'date_id': self.date_id,
            'time_id': self.time_id,
            'view_count': self.view_count,
            'like_count': self.like_count,
            'comment_count': self.comment_count
        }
