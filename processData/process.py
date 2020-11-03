import pandas as pd
import numpy as np

QUANHUYEN = [
    'Hoàn Kiếm',
    'Đống Đa',
    'Ba Đình',
    'Hai Bà Trưng',
    'Hoàng Mai',
    'Thanh Xuân',
    'Long Biên',
    'Nam Từ Liêm',
    'Bắc Từ Liêm',
    'Tây Hồ',
    'Cầu Giấy',
    'Hà Đông',
    'Sơn Tây',
    'Ba Vì',
    'Chương Mỹ',
    'Phúc Thọ',
    'Đan Phượng',
    'Đông Anh',
    'Gia Lâm',
    'Hoài Đức',
    'Mê Linh',
    'Mỹ Đức',
    'Phú Xuyên',
    'Quốc Oai',
    'Sóc Sơn',
    'Thạch Thất',
    'Thanh Oai',
    'Thường Tín',
    'Ứng Hòa',
    'Thanh Trì'
]

dff = pd.read_csv('/Users/khanhkd/Desktop/Github_kieuduykhanh/PxKteam/crawlDataFrom_batdongsan_com_vn/data_crawl_from_web/apartments.csv')


def processData(dataFrame):
    acreage = dataFrame['acreage'].str.extract('(\d+.?\d*)').astype(float)
    dataFrame['acreage'] = acreage
    typrice = dataFrame['price'].str.contains("tỷ")
    # lay gia tri co chu ty ra

    trieuprice = dataFrame['price'].str.endswith('iệu')

    floattyprice = dataFrame[typrice]['price'].str.extract('(\d+.?\d*)').astype(float) * 1000
    # Lay tu typrice ra va *1000 de tinh sang trieu

    pricetom = floattyprice.div(dataFrame[typrice][['acreage']].values)
    # quy tien ty ve tien trieu

    dataFrame['pricePerM'] = dataFrame['price'].copy()
    # copy ra 1 col moi

    dataFrame['pricePerM'] = dataFrame['pricePerM'].str.extract('(\d+.?\d*)').astype(float)
    # covert bang ve so


    for district in QUANHUYEN:
        district_ = dataFrame.address.str.lower().str.contains(district.lower())
        dataFrame.loc[district_, 'district'] = district


    dataFrame['pricePerM'].update(pricetom[0])
    # update la bang pricetom bang gia/m

    giatrieu = dataFrame[trieuprice & (dataFrame['pricePerM'] > 200)]['pricePerM']
    trieuToM = giatrieu.div(dataFrame[trieuprice & (dataFrame['pricePerM'] > 200)]['acreage'].values)

    dataFrame['pricePerM'].update(trieuToM)

    numBathroom = dataFrame['numBathroom'].str.extract('(\d+)').astype(float)
    numBedroom = dataFrame['numBedroom'].str.extract('(\d+)').astype(float)

    dataFrame['numBathroom'] = numBathroom
    dataFrame['numBedroom'] = numBedroom

    locations = dataFrame.location.str.strip('[]').str.split(',')

    latitude = []
    longitude = []
    for i in locations:
        latitude.append(float(i[0]))
        longitude.append(float(i[1]))

    dataFrame['lat'] = latitude
    dataFrame['long'] = longitude

    dataFrame['date'] = pd.to_datetime(dataFrame['date'], dayfirst=True)

    dataFrame['quarters'] = dataFrame['date'].dt.quarter
    # Thêm quý trong năm

    # chc[(chc['pricePerM'].isnull()) & (chc['price'].str.contains('thuận'))][['pricePerM', 'price', 'acreage']].index

    df = dataFrame.drop(columns=['service', 'facade', 'wayIn', 'contact', 'linkProject', 'location'])

    df = df.drop(df[df['pricePerM'].isnull()][['pricePerM', 'price', 'acreage']].index)

    return df

dff = processData(dff)


