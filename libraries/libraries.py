from connectDB.model import Apartments

def standardizedData(obj):
    try:
        obj = obj.__dict__
    except:
        return None
    try:
        if '_sa_instance_state' in obj:
            del obj["_sa_instance_state"]
    except:
        pass
    if obj['images'] != None:
        obj['images'] = obj['images'].split(', ')
    return obj


def checkDataString(data, cols):
    if data[cols] == '' or data[cols] == '[]' or data[cols] == None:
        return None
    elif cols == 'images':
        return data[cols][1:-1].replace("'", '')
    return data[cols].lower()


def checkDataNumber(data, cols):
    if data[cols] == '' or data[cols] == None:
        return None
    return float(data[cols])


def getDefault(parameters, metadata, obj):
	if ('orderBy' or 'orderType') not in parameters:
		order = obj.id.asc()
	else:
		try:
			if parameters['orderType'] == 'desc':
				order = metadata[parameters['orderBy']].desc()
			else:
				order = metadata[parameters['orderBy']].asc()
		except:
			order = obj.id.asc()
	if 'limit' not in parameters:
		limit = 10
	else:
		try:
			limit = int(parameters['limit'])
		except:
			limit = 10
	if 'page' not in parameters:
		page = 1
	else:
		try:
			page = int(parameters['page'])
		except:
			page = 1
	offset = (page - 1) * limit

	colsNum = {}
	colsStr = {}

	for col in Apartments.__table__.columns:
		if str(col) in parameters:
			if str(col) ==' apartments.acreage' or str(col) ==' apartments.price' or str(col) == ' apartments.numBedroom' \
					or str(col) == ' apartments.numBathroom':
				colsNum[str(col)] = parameters[float(col)]
			else:
				colsStr[str(col)] = parameters[str(col)]


	return limit, page, offset, order, colsStr, colsNum