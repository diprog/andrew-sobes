import json


class JSONable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
