from app.models.database import *


def getUser(args):
    db = Database()
    query = 'SELECT * FROM "USER_INFO" WHERE "LOGIN_ID" = %s AND "LOGIN_PW" = %s'
    param = [args.get('loginId'), args.get('password')]
    result = db.excuteReadQuery(query, param)

    returndata = {'errorcode': 1, 'msg': 'invalid ID or Password'}
    if result:
        returndata = {'errorcode': 0,
                      'msg': 'exist user',
                      'userId': result[0][1],
                      'password': result[0][4],
                      'email': result[0][0],
                      'userNm': result[0][2]
                      }

    db.closeConnection()

    return returndata


def registUser(args):
    db = Database()

    query = 'SELECT * FROM "USER_INFO" WHERE "LOGIN_ID" = %s'
    param = [args.get('loginId')]
    result = db.excuteReadQuery(query, param)

    if result:
        db.closeConnection()
        return {'errorcode': 1,
                'msg': args.get('loginId') + ' already exist user.'
               }

    query = 'INSERT INTO public."USER_INFO"("EMAIL", "LOGIN_ID", "NAME", "USER_ID", "LOGIN_PW", "DEL_YN", "INS_USER_ID", "INS_DTM")VALUES (%s, %s, %s, (SELECT \'USER\'||SUBSTRING(COALESCE(MAX("USER_ID"), \'USER000000\'), 5, 6)::INTEGER + 1 FROM public."USER_INFO")::TEXT, %s, %s, %s, current_timestamp);'
    param = [args.get('email'), args.get('loginId'), args.get('name'), args.get('password'), "N", "ADMIN"]
    db.excuteWriteQuery(query, param)
    db.conn.commit()
    db.closeConnection()
    return {'errorcode': 0,
            'msg': 'Successfully registered.'
           }
