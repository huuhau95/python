from connectDB.model import ConnectToDB, Apartments
from libraries.libraries import checkDataString, checkDataNumber

Session = ConnectToDB()

def post(data):
    '''
    Push data to database
    :param data:
    :return:
    '''
    try:
        session = Session()
        apartment = Apartments(
            tileProduct = checkDataString(data, 'tileProduct'),
            date = checkDataString(data, 'date'),
            images = checkDataString(data, 'images'),
            acreage = checkDataNumber(data, 'acreage'),
            investor = checkDataString(data, 'investor'),
            juridical = checkDataString(data, 'juridical'),
            price = checkDataNumber(data, 'pricetom'),
            numBedroom = checkDataNumber(data, 'numBedroom'),
            furniture = checkDataString(data, 'juridical'),
            numBathroom = checkDataNumber(data, 'numBathroom'),
            description = checkDataString(data, 'description'),
            nameProject = checkDataString(data, 'nameProject'),
            address = checkDataString(data, 'address'),
            farCenter = checkDataNumber(data, 'farCenter'),
            lat = checkDataNumber(data, 'lat'),
            long = checkDataNumber(data, 'long')
        )
        session.add(apartment)
        try:
            session.commit()
        except Exception as exp:
            raise (exp)
            print('error1')
        print('ok')
    except Exception as exp:
        raise (exp)
        print('error2')
    finally:
        session.close()




import csv
# read csv file as type json format
reader = csv.DictReader(open("/Users/khanhkd/Desktop/Github_kieuduykhanh/PxKteam/crawlDataFrom_batdongsan_com_vn/data_crawl_from_web/datapxk.csv"))

apartments = []
for raw in reader:
    apartments.append(raw)

for i in range(len(apartments)):
    try:
        post(apartments[i])
    except:
        pass

