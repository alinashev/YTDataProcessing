from typing import Any
from keys import keys


class APIkey:
    def __init__(self) -> None:
        self.list_k = keys

    def get_key(self, current_key="", next_key="false") -> Any:

        if len(self.list_k) > 0:
            if next_key == "true":
                self.list_k.remove(current_key)
            return self.list_k[0]
        else:
            print("NO LIVE KEYS")

