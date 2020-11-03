from crawlDataFrom_batdongsan_com_vn.Apartment import Apartment
from bs4 import BeautifulSoup
import urllib.request
import csv

def getAllLinkApartmentsFromPage(link):
    '''
    lấy all link trong 1 page
    :param link:
    :return:
    '''
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    classes = soup.findAll('div', class_="ct_title")
    for i in range(len(classes)):
        classes[i] = 'https://alonhadat.com.vn' + classes[i].find('a').get('href')
    return classes

def getAllLink(endPage = 171):
    '''
    lấy all link trong 171 page
    :param endPage:
    :return:
    '''
    listLinkApartments = []
    startPage = 1
    while startPage <= endPage:
        try:
            listLinkApartments += getAllLinkApartmentsFromPage('https://alonhadat.com.vn/nha-dat/can-ban/can-ho-chung-cu/1/ha-noi/trang--{}.html'.format(startPage))
            startPage += 1
        except:
            continue
    return listLinkApartments

def handlingApartment(ApartmentUrl):
    '''
    :param ApartmentUrl: url of an apartment
    :return: object Apartment
    '''

    page = urllib.request.urlopen(ApartmentUrl)
    soup = BeautifulSoup(page, 'html.parser')
    apartment = Apartment()
    apartment = addAttributesToObject(soup, apartment)
    return apartment

def addAttributesToObject(soup, object):
    allAttributes = soup.find('div', class_="property")

    try: object.tileProduct = allAttributes.find('div', class_="title").find('h1').text.strip()
    except: pass
    try: object.date = allAttributes.find('div', class_="title").find('span', class_="date").text.strip()
    except: pass
    try: object.description = allAttributes.find('div', class_="detail text-content").text.strip()
    except: pass
    try: object.price = allAttributes.find('div', class_="moreinfor").find('span', class_="price").find('span', class_="value").text.strip()
    except: pass
    try: object.acreage = allAttributes.find('div', class_="moreinfor").find('span', class_="square").find('span', class_="value").text.strip()
    except: pass
    try: object.address = allAttributes.find('div', class_="address").find('span', class_="value").text.strip()
    except: pass
    try:
        for key in location.keys():
            if key in object.address.lower():
                object.location = location[key]
    except: pass
    try: object.linkProject = 'https://alonhadat.com.vn' + allAttributes.find('span', class_="project").find('a').get('href')
    except: pass
    try:
        trs = allAttributes.find('div', class_="moreinfor1").find('div', class_="infor").findAll('tr')
        lis = []
        for tr in trs:
            for td in tr.findAll('td'):
                lis.append(td.text)
        for i in range(len(lis)):
            if lis[i].lower() == 'hướng':
                object.directionHome = lis[i+1]
            elif lis[i].lower() == 'pháp lý':
                object.juridical = lis[i+1]
            elif lis[i].lower() == 'số phòng ngủ':
                object.numBedroom = lis[i+1]
    except: pass
    try:
        for span in allAttributes.find('div', class_="image-list").findAll('span'):
            object.images.append('https://alonhadat.com.vn' + span.find('img').get('src'))
    except: pass
    try:
        page2 = urllib.request.urlopen(object.linkProject)
        soup2 = BeautifulSoup(page2, 'html.parser')
        try:
            object.sizeProject = soup2.find('div', id="ctl00_content_pc_project_content").text.lower()
        except: pass
    except: pass
    return object

def writeDataToCSV(apartmentList):
    with open('apartmentsAloNhaDat.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['tileProduct', 'date', 'images', 'acreage', 'contact', 'location', 'investor', 'juridical',
                         'price', 'numBedroom', 'directionHome', 'directionBalcony', 'service', 'furniture',
                         'numBathroom',
                         'description', 'facade', 'wayIn', 'nameProject', 'keyWords', 'address', 'sizeProject',
                         'farCenter',
                         'linkProject'])
        for apartment in apartmentList:
            writer.writerow(
                [apartment.tileProduct, apartment.date, apartment.images, apartment.acreage, apartment.contact,
                 apartment.location, apartment.investor, apartment.juridical, apartment.price, apartment.numBedroom,
                 apartment.directionHome, apartment.directionBalcony, apartment.service, apartment.furniture,
                 apartment.numBathroom, apartment.description, apartment.facade, apartment.wayIn, apartment.nameProject,
                 apartment.keyWords, apartment.address, apartment.sizeProject, apartment.farCenter,
                 apartment.linkProject])

location = {
    'hoàn kiếm' : [21.028889, 105.8525],
    'đống đa' : [21.0157, 105.856],
    'ba đình' : [21.0367, 105.836],
    'hai bà trưng' : [21.011718, 105.847647],
    'hoàng mai' : [20.968072, 105.848207],
    'thanh xuân' : [20.993445, 105.798454],
    'long biên' : [21.004167, 105.969444],
    'nam từ liêm' : [21.003333, 105.703889],
    'bắc từ liêm' : [21.054167, 105.682222],
    'tây hồ' : [21.070705, 105.811831],
    'cầu giấy' : [21.030938, 105.801312],
    'hà đông' : [20.964944, 105.770694],
    'sơn tây' : [21.138947, 105.504402],
    'ba vì' : [21.066667, 105.334722],
    'chương mỹ' : [20.9242, 105.702],
    'phúc thọ' : [21.108611, 105.536944],
    'đan phượng' : [21.0875, 105.667222],
    'đông anh' : [21.132987, 105.835155],
    'gia lâm' : [21.019788, 105.937332],
    'hoài đức' : [21.04, 105.43],
    'mê linh' : [21.187222, 105.715278],
    'mỹ đức' : [20.684167, 105.7425],
    'phú xuyên' : [20.74, 105.907778],
    'quốc oai' : [20.97055556, 105.6113889],
    'sóc sơn' : [21.257521, 105.848529],
    'thạch thất' : [21.03055556, 105.5691667],
    'thanh oai' : [20.855556, 105.765],
    'thường tín' : [20.845189, 105.87836],
    'ứng hoà' : [20.726, 105.7713],
    'thanh trì' : [20.949444, 105.843333]
}

# print(location.keys())

apartments = []

for link in getAllLink():
    apartments.append(handlingApartment(link))

writeDataToCSV(apartments)