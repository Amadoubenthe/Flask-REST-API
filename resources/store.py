from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

from models.stores import StoreModel

class Store(Resource):
	def get(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return store.json()

		return {'message': 'Store not found'}, 404

	def post(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return{'message': 'A store with "{}" name already exist'.format(name)}

		store = StoreModel(name)

		try:
			store.save_to_db()
		except:
			return {'message': 'An error occured while creating the store.'}, 201

		return {'message': 'Store created succefuly.'}	

	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete()

		return {'message': 'Store deleted'}

class StoreList(Resource):
	def get(self):
		return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
		# return {'message': [x.json() for x in StoreModel.query.all()]}
