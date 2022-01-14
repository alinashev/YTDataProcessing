from keys import keys


class APIkey:
    def get_key(self, next_key="false"):
        list_k = keys
        if next_key == "true":
            del list_k[0]
            return list_k[0]
        else:
            next_key = "false"
            return list_k[0]

