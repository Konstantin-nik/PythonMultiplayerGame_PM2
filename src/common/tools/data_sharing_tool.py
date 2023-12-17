import json
import re

from src.game.constants.constants import DATA_START_STRING, DATA_END_STRING
from src.common.tools.get_class_by_name import get_class_by_name


class DataSharingTool:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.data_string = ''
            self._initialized = True

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.next()
        except StopIteration:
            raise StopIteration

    def next(self):
        if self.data_string is None or self.data_string == '':
            raise StopIteration

        pattern = r'{DATA_START_STRING}(.*?){DATA_END_STRING}'.format(
            DATA_START_STRING=DATA_START_STRING, DATA_END_STRING=DATA_END_STRING)
        matches = re.search(pattern=pattern, string=self.data_string)
        if matches is None:
            raise StopIteration

        self.data_string = self.data_string[self.data_string.find(DATA_END_STRING) + len(DATA_END_STRING):]

        return self.from_json(matches[1])

    @staticmethod
    def from_json(json_str: str):
        obj_dict = json.loads(json_str)
        name = obj_dict['name']
        data = obj_dict['data']
        cls = get_class_by_name(name)
        if cls is None:
            return None
        return name, cls.from_json(data)

    @staticmethod
    def to_json(obj) -> str:
        """
        Method to get objects ready to send
        :param obj:
        :return:
        """
        json_str = json.dumps({
            'name': obj.NAME,
            'data': obj.to_json()
        })
        return DATA_START_STRING + json_str + DATA_END_STRING

    def add_data(self, data: str):
        self.data_string += data


# if __name__ == '__main__':
#     player1 = Player("Sergey", 10, 20)
#     player2 = Player("Masha", 10, 20)
#     player3 = Player("Petya", 10, 20)
#
#     data_sharing_tool = DataSharingTool()
#
#     p_json = DataSharingTool.to_json(player1)
#     data_sharing_tool.add_data(p_json)
#
#     p_json = DataSharingTool.to_json(player2)
#     data_sharing_tool.add_data(p_json)
#
#     data_sharing_tool.add_data("something_strange")
#     p_json = DataSharingTool.to_json(player3)
#     data_sharing_tool.add_data(p_json)
#     # data_sharing_tool.data_string = data_sharing_tool.data_string[:32] + '-' + data_sharing_tool.data_string[33:]
#     # data_sharing_tool.data_sting = data_sharing_tool.data_sting[:-7]
#
#     for data in data_sharing_tool:
#         print(data)

    # print(data_sharing_tool.data_sting)
