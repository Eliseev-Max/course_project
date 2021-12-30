import MySQLdb


class SQL_client():

    def __init__(self, host, db, port=3306, charset="utf8"):
        self.host = host
        self.db = db
        self.port = port
        self.charset = charset
        self.is_connected = False

    def connect(self, user, password):
        # self.user = user
        # self.pwd = password
        try:
            self.con = MySQLdb.connect(user=user,
                                   passwd=password,
                                   host=self.host,
                                   port=self.port,
                                   db=self.db,
                                   charset=self.charset
                                   )
        except Exception as err:
            print(f"Not connected to the database {self.db}: {err}")
        else:
            self.is_connected = True

    def disconnect(self):
        if self.is_connected:
            self.con.close()
        else:
            print("Database connection does not exist")

    def create_cursor(self):
        if self.is_connected:
            self.cursor = self.con().cursor()
        else:
            raise Exception("Impossible to create cursor object!\nDatabase connection does not exist")

    def execute_query(self, query):
        pass
