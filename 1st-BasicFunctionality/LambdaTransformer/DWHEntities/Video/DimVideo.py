class DimVideo:
    def __init__(self, video_id: str, channel_id: str, channel_name: str,
                 title: str, description: str, category_id: str) -> None:
        self.video_id: str = video_id
        self.channel_id: str = channel_id
        self.channel_name: str = channel_name
        self.title: str = title
        self.description: str = description
        self.category_id: str = category_id

    def __str__(self) -> str:
        return 'video_id {video_id}' \
               '\nchannel_id {channel_id}' \
               '\nchannel_name {channel_name}' \
               '\ntitle {title}' \
               '\ndescription {description}' \
               '\ncategory_id {category_id}'.format(video_id=self.video_id,
                                                    channel_id=self.channel_id,
                                                    channel_name=self.channel_name,
                                                    title=self.title,
                                                    description=self.description,
                                                    category_id=self.category_id)

    def to_dict(self) -> dict:
        return {
            'video_id': self.video_id,
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'title': self.title,
            'description': self.description,
            'category_id': self.category_id
        }
