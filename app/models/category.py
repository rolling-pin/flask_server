from app.models.database import *
import json


def getTotalFavorite(args):
    db = Database()

    query = 'SELECT "CTGRY_CD", "CTGRY_NM" FROM "CTGRY_MASTER" WHERE "DEL_YN" = \'N\''
    result = db.excuteReadQuery(query, [])
    print(result)
    print(type(result[0]))
    if result:
        returndata = json.dumps(result, indent=2)
    else:
        returndata = {'errorcode': -1, 'msg': 'Failed to get category info.'}

    db.closeConnection()

    return returndata
