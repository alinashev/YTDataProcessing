import json
import os.path


class ReaderJSON:
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError('File not found')
        self.path = path

    def open(self) -> dict:
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                text = json.load(f)
            except ValueError as e:
                raise ValueError('Invalid json: {}'.format(e)) from None
        return text

    def get_json(self) -> dict:
        return ReaderJSON.open(self)