import psycopg2
from psycopg2.extras import RealDictCursor


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
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def excuteWriteQuery(self, query, param):
        self.cur.execute(query, param)
        return True

    def excuteReadQuery(self, query, param):
        self.cur.execute(query, param)
        return self.cur.fetchall()

    def closeConnection(self):
        self.conn.close()



