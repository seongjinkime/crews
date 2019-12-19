import json
import os

class Crews(object):
    sql_manager = None
    data = None
    json_path = None

    def __init__(self, sql_manager):
        self.sql_manager = sql_manager
        self.json_path = "cache/2019_12_07_crews.json"
        self.data = {}

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
        print("WRITE JSON")
        print(self.data)
        with open(self.json_path, 'w') as out:
            json.dump(self.data, out)

    def update(self, crews):
        phones = crews['phones']
        for p in phones:
            self.add_phone(p)

        self.clean_unregistered(phones)

    def clean_unregistered(self, registered):
        cnt = 0
        for p in self.get_all_phones():
            if p not in registered and p in self.data:
                cnt += 1
                del(self.data[p])

        if cnt > 0:
            self.write_json()


    def get_all_phones(self):
        phones = []
        for p in self.data.keys():
            phones.append(p)
        return phones

    def add_phone(self, phone, name=None):
        if phone in self.get_all_phones():
            return

        if name is None:
            try:
                name = (self.sql_manager.get_user_by_phone(phone)).get_name()
            except Exception as e:
                print(str(e))
                return

        self.data[phone] = {'name': name,
                            'note': "",
                            'send_msg': False
                            }
        self.write_json()







