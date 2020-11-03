from crawlDataFrom_batdongsan_com_vn.functionCrawl import *

url = 'https://batdongsan.com.vn/ban-dat-nen-du-an-duong-419-xa-binh-yen-1/ban-gap-gan-khu-cong-nghe-cao-hoa-lac-pr27244126'




apartments = []
projectLands = []
for link in getAllLinkApartmentsFromBDS_com_vn(endPage=2):
    apartments.append(handlingApartment(link))

for link in getAllLinkProjectLandsFromBDS_com_vn(endPage=2):
    projectLands.append(handlingProjectLand(link))

writeDataToCSV(apartments, projectLands)