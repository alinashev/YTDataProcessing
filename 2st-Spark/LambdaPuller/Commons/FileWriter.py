import json


class FileWriter:
    def __init__(self, path: str) -> None:
        self.path = path

    def writing(self, data: dict) -> None:
        with open(self.path, 'w') as f:
            json.dump(data, f)

    def get_path(self) -> str:
        return self.path
