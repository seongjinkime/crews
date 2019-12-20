
class User(object):

    phone = None
    name = None
    sex = None
    address = None
    registration = None
    history = None
    visit_count = None
    emergency = None


    def __init__(self):
        pass

    def parse_data_using_dict(self, data):
        self.set_phone(data['phone'])
        self.set_name(data['name'])
        self.set_address(data['address'])
        self.set_registration(data['registration'])
        self.set_sex(data['sex'])
        self.set_visit_count(data['visitCount'])
        self.set_emergency(data['emergency'])

        if 'history' in data:
            self.set_history(data['history'])

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_registration(self):
        return self.registration

    def set_registration(self, registration):
        self.registration = registration

    def get_history(self):
        return self.history

    def set_history(self, history):
        self.history = history

    def get_visit_count(self):
        return self.visit_count

    def set_visit_count(self, count):
        self.visit_count = count

    def get_emergency(self):
        return self.emergency

    def set_emergency(self, emergency):
        self.emergency = emergency

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex
