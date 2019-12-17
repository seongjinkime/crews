import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from model.user import User

class FBManager(object):

    registration = None
    date = "2019/12/07"

    def __init__(self):
        print("FB Manager init")

    def auth_db(self):
        print("Auth Realtime Database")
        cred = credentials.Certificate("database/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://fishingmanager-4f88b.firebaseio.com'
        })

    def get_users(self):
        return db.reference("users").get()

    def register_callback_of_crews(self, func):
        self.registration = db.reference("crews/{0}".format(self.date)).listen(func)

    def add_empty_crews(self):
        empty = {'date' : '2019/12/08', 'phones' : [], 'total' : 0}
        db.reference("crews/{0}".format(self.date)).update(empty)

    def get_full_informations(self, phones):
        users = []
        for p in phones:
            data = db.reference("users/{0}".format(p)).get()
            user = User()
            user.parse_data_using_dict(data)
            users.append(user)
        return users



    def close(self):
        try:
            self.registration.close()
        except Exception as e:
            print(str(e))
