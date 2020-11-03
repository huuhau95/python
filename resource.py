from flask import Flask
from flask_restful import Api


from connectDB.ApartmentsAPI import ApartmentsCollectionAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(ApartmentsCollectionAPI, '/apartments', methods = ['GET', 'POST'])

if __name__ == '__main__':
	try:
		app.run(host='https://hau-dev.herokuapp.com', port=3001, debug=True)
	except Exception as exp:
		print (exp)