from app.models.database import *
import json


def getTotalFavorite(args):
    db = Database()

    query = 'SELECT "CTGRY_CD", "CTGRY_NM" FROM "CTGRY_MASTER" WHERE "DEL_YN" = \'N\''
    result = db.excuteReadQuery(query, [])
    if result:
        returndata = json.dumps(result, indent=2)
    else:
        returndata = {'errorcode': -1, 'msg': 'Failed to get category info.'}

    db.closeConnection()
    return returndata

def getUserFavorite(args):
    db = Database()

    query = 'SELECT "USER_ID", "CTGRY_CD" FROM "USER_FAVORITE" WHERE "USER_ID" = %s AND "DEL_YN" = \'N\''
    param = [args.get('userId')]
    result = db.excuteReadQuery(query, param)
    if result:
        returndata = json.dumps(result, indent=2)
    else:
        returndata = {'errorcode': -1, 'msg': 'Failed to get category info.'}

    db.closeConnection()
    return returndata


def registUserFavorite(args):
    print(args)
    db = Database()
    query = 'DELETE FROM public."USER_FAVORITE" WHERE "USER_ID" = %s;'
    param = [args.get('userId')]
    db.excuteWriteQuery(query, param)

    ctgryCds = args.get('ctgryCd')
    for val in ctgryCds:
        query = 'INSERT INTO public."USER_FAVORITE"("USER_ID", "CTGRY_CD", "DEL_YN", "INS_USER_ID", "INS_DTM")VALUES (%s, %s, %s, %s, current_timestamp);'
        param = [args.get('userId'), val, "N", args.get('userId')]
        db.excuteWriteQuery(query, param)

    db.conn.commit()
    db.closeConnection()
    return {'errorcode': 0,
            'msg': 'Successfully registered.'
           }
