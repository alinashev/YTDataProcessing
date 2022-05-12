class Configurator:
    def __init__(self) -> None:
        self.s3_general_agg_dir = "StreamingOutput/"

    def longest_agg(self) -> dict:
        return {
            "param": "length",
            "out_dir": self.s3_general_agg_dir + "longestComment"
        }

    def most_liked_agg(self) -> dict:
        return {
            "param": "like",
            "out_dir": self.s3_general_agg_dir + "mostLikedComment"
        }

    def most_replied_agg(self) -> dict:
        return {
            "param": "reply",
            "out_dir": self.s3_general_agg_dir + "mostRepliedComment"
        }

    def get_all_aggregate_params(self) -> list:
        return [self.longest_agg(),
                self.most_liked_agg(),
                self.most_replied_agg()
                ]

