from Commons.keys import keys


class APIkey:
    def __init__(self) -> None:
        self.keys_list = keys

    def get_key(self, current_key: str = "", next_key: bool = False) -> str:
        if len(self.keys_list) > 0:
            if next_key:
                self.keys_list.remove(current_key)
            return self.keys_list[0]
        else:
            print("No valid keys")
