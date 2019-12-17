import json
import os

class Crews(object):
    sql_manager = None
    data = None
    json_path = None

    def __init__(self, sql_manager):
        self.sql_manager = sql_manager
        self.json_path = "cache/2019_12_07_crews.json"

    def init_data(self):
        if not os.path.exists(self.json_path):
            self.create_json()

        with open(self.json_path) as json_file:
            self.data = json.load(json_file)

        print("crews init")
        print(self.data)

    def get_data(self):
        return self.data

    def create_json(self):
        self.data = {}
        self.write_json()

    def write_json(self):
        with open(self.json_path, 'w') as out:
            json.dump(self.data, out)

    def update(self, crews):
        phones = crews['phones']
        for p in phones:
            if p in self.get_all_phones():
                continue
            else:
                self.add_phone(p)

    def get_all_phones(self):
        return self.data.keys()

    def add_phone(self, phone):
        try:
            user = self.sql_manager.get_user_by_phone(phone)

            self.data[phone] = {'name': user.get_name(),
                                'note': "",
                                'send_msg': False
                                }
            self.write_json()

        except Exception as e:
            print(str(e))







