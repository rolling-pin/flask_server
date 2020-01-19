import psycopg2


class Database:
    def __init__(self):
        super().__init__()
        if not hasattr(self, 'conn'):
            host = "rollingpin-db.caduakykgikn.ap-northeast-2.rds.amazonaws.com"
            dbname = "postgres"
            user = "rollingpin"
            password = "rollingpin"
            connectionInfo = "host= %s dbname= %s user= %s password= %s" % (host, dbname, user, password)
            self.conn = psycopg2.connect(connectionInfo)
            self.cur = self.conn.cursor()

    def excuteQuery(self, query, param):
        print(query)
        print(type(query))
        self.cur.execute(query, param)
        return self.cur.fetchall()

    def closeConnection(self):
        self.conn.close()



