import psycopg2


class Database:
    def __init__(self):
        super().__init__()
        host = "rollingpin-db.caduakykgikn.ap-northeast-2.rds.amazonaws.com"
        dbname = "postgres"
        user = "rollingpin"
        password = "rollingpin"
        connectionInfo = "host= %s dbname= %s user= %s password= %s" % (host, dbname, user, password)
        connection = psycopg2.connect(connectionInfo)
        self.cur = connection.cursor()

    def excuteQuery(self, query, param):
        print(query)
        print(type(query))
        self.cur.execute(query, param)
        return self.cur.fetchall()




