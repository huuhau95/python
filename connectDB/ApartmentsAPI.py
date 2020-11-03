from connectDB.model import ConnectToDB, Apartments
from flask_restful import Resource
from flask import request
from sqlalchemy import or_, and_
from libraries.libraries import standardizedData, getDefault

Session = ConnectToDB()

class ApartmentsCollectionAPI(Resource):
    def get(self):
        try:
            session = Session()
            parameters = request.args
            limit, page, offset, order, colsStr, colsNum = getDefault(
                parameters, Apartments.__table__.columns, Apartments
            )

            apartments = session.query(Apartments)


            apartments = apartments.filter(and_(key.like('%' + colsStr[str(key)] + '%') \
                                               for key in Apartments.__table__.columns \
                                               if str(key) in colsStr.keys()))

            apartments = apartments.filter(and_(key.between(int(colsNum[str(key)]), int(colsNum[str(key)]) + 1) \
                                               for key in Apartments.__table__.columns \
                                               if str(key) in colsNum.keys()))


            apartments = apartments.order_by(order).offset(offset).limit(limit).all()
            for i in range(len(apartments)):
                apartments[i] = standardizedData(apartments[i])
            return apartments
        except Exception as exp:
            raise (exp)
            return []
        finally:
            session.close()


    def post(self):
        data = request.get_json()
        return fake_model(data['date'], data['acreage'], data['numBedroom'], data['numBathroom'], data['farCenter'],
                          data['district'], data['investor'], data['type'])


def fake_model(date, acreage, numBedroom, numBathroom, farCenter, district, investor, type):
    return 25.3


