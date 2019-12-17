import sqlite3
from model.user import User


def not_dict(data):
    return str(type(data)) != "<class 'dict'>"

class SQLManager(object):
    """
    TABLE STRUCTURE
    PHONE | NAME |
    """
    conn = None
    db_path = "database/users.db"
    table = "USERS"

    def __init__(self):
        print("SQL Manager init")

    def connect_db(self):
        print("Connect sql")
        self.conn = sqlite3.connect(self.db_path)

    def init_table(self):
        c = self.conn.cursor()
        #cmd = "CREATE TABLE IF NOT EXISTS {0} (".format(self.table)
        #cmd += "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        cmd = "DROP TABLE IF EXISTS {0}".format(self.table)
        c.execute(cmd)
        cmd = "CREATE TABLE IF NOT EXISTS {0} (".format(self.table)
        cmd += "PHONE TEXT PRIMARY KEY, "
        cmd += "NAME TEXT "
        cmd += " );"
        c.execute(cmd)
        c.execute("DELETE FROM " + self.table)
        c.close()

    def insert_users(self, users):
        c = self.conn.cursor()

        #if null or not dict
        if users is None or not_dict(users):
            return

        # info keys : name, phone, regisration, visitCount
        infos = []
        for phone, info in users.items():
            infos.append((info['phone'], info['name']))
            print(infos[len(infos)-1])

        cmd = "INSERT INTO {0} VALUES (?,?)".format(self.table)
        c.executemany(cmd, infos)
        self.conn.commit()
        c.close()
        print("Sync Ok")

    def get_user_by_phone(self, phone):
        print(phone)
        c = sqlite3.connect(self.db_path).cursor()
        cmd = "SELECT * FROM {0} WHERE PHONE = '{1}';".format(self.table, phone)
        c.execute(cmd)
        data = c.fetchone()
        user = User()
        user.set_phone(data[0])
        user.set_name(data[1])
        return user

