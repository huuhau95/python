from crawlDataFrom_batdongsan_com_vn.functionCrawl import *


urlApartmentOfHanoi = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi/p'
urlProjectLandsOfHanoi = 'https://batdongsan.com.vn/ban-dat-nen-du-an-ha-noi/p'


apartments = []
projectLands = []
for link in getAllLinkApartmentsFromBDS_com_vn():
    apartments.append(handlingApartment(link))

for link in getAllLinkProjectLandsFromBDS_com_vn():
    projectLands.append(handlingProjectLand(link))

writeDataToCSV(apartments, projectLands)
